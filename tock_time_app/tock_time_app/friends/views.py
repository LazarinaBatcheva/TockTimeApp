from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from tock_time_app.accounts.models import Profile
from tock_time_app.friends.choices import FriendRequestStatusChoices
from tock_time_app.friends.models import FriendRequest
from tock_time_app.friends.serializers import FriendRequestSerializer

UserModel = get_user_model()


class FriendsDashboardView(LoginRequiredMixin, ListView):
    """ View for displaying a paginated list of friend requests. """

    model = FriendRequest
    template_name = 'friends/friends-dashboard.html'
    paginate_by = 10


class FriendRequestViewSet(LoginRequiredMixin, ModelViewSet):
    """ ViewSet for managing friend requests, including creating, listing, and updating. """

    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer

    def get_queryset(self):
        """
        Customize the queryset based on the action being performed.
        For 'list' action, only pending requests for the current user are returned.
        """

        if self.action == 'list':

            return self.queryset.filter(
                receiver=self.request.user,
                status=FriendRequestStatusChoices.PENDING,
            )

        return super().get_queryset()

    def create(self, request, *args, **kwargs):
        """
        Create a friend request.
        - Validates that the user is not sending a request to themselves.
        - Ensures that the users are not already friends.
        - Deletes old requests (if any) before creating a new one.
        """

        receiver_username = request.data.get('receiver_username')
        receiver = get_object_or_404(UserModel, username=receiver_username)

        # Check if the user is trying to send a friend request to themselves
        if receiver == request.user:
            return Response(
                {'detail': 'You cannot send a friend request to yourself!'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Check if the user is trying to send a friend request to an existing friend
        if request.user.profile.friends.filter(pk=receiver.profile.pk).exists():
            return Response(
                {'detail': 'You are already friends with this user!'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Check if a friend request already exists.
        existing_request = FriendRequest.objects.filter(
            sender=request.user,
            receiver=receiver,
        ).first()

        if existing_request:
            if existing_request.status == FriendRequestStatusChoices.PENDING:

                return Response(
                    {'detail': 'Friend request already sent and is pending!'},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            elif (existing_request.status in
                  [FriendRequestStatusChoices.ACCEPTED, FriendRequestStatusChoices.REJECTED]):

                existing_request.delete()

        # Create a new friend request.
        friend_request = FriendRequest.objects.create(
            sender=request.user,
            receiver=receiver,
        )
        serializer = self.get_serializer(friend_request)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        """
        Update a friend request (accept or reject).
        - Accepting: Adds the users as friends.
        - Rejecting: Updates the status without adding friends.
        """

        friend_request = get_object_or_404(
                FriendRequest,
                pk=kwargs['pk'],
                receiver=request.user,
        )
        status_action = request.data.get('status')

        # Check if the status is valid.
        if (status_action not in
                [FriendRequestStatusChoices.ACCEPTED, FriendRequestStatusChoices.REJECTED]):
            return Response(
                {'detail': 'Invalid status!'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if status_action == FriendRequestStatusChoices.ACCEPTED:
            sender_profile = friend_request.sender.profile
            receiver_profile = friend_request.receiver.profile

            sender_profile.friends.add(receiver_profile)
            receiver_profile.friends.add(sender_profile)

        # Update the friend request status.
        friend_request.status = status_action
        friend_request.save()

        return Response(
            {'detail': f'Friend request {status_action} successfully!'},
            status=status.HTTP_200_OK,
        )


class FriendRemoveViewSet(LoginRequiredMixin, ViewSet):
    """ ViewSet for removing friends. """

    def destroy(self, request, *args, **kwargs):
        """
        Remove a friend relationship between two users.
        - Ensures that the profiles are friends before removing the relationship.
        """

        friend_pk = kwargs.get('pk')
        friend_profile = get_object_or_404(Profile, pk=friend_pk)

        # Check if the profiles are friends
        if not request.user.profile.friends.filter(pk=friend_profile.pk).exists():
            return Response(
                {'detail': 'You are not friends with this user!'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Remove friendship
        request.user.profile.friends.remove(friend_profile)
        friend_profile.friends.remove(request.user.profile)

        return Response(
            {'detail': 'Friend removed successfully!'},
            status=status.HTTP_200_OK,
        )