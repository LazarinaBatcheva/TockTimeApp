from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tock_time_app.friends import views

# Create a router for REST API routes
router = DefaultRouter()
router.register(r'friend-requests', views.FriendRequestViewSet, basename='friend-requests')
router.register(r'friends-remove', views.FriendRemoveViewSet, basename='friends-remove')

urlpatterns = [
    # Dashboard view for managing friends
    path('<str:username>/', include([
        path('', views.FriendsDashboardView.as_view(), name='friends-dashboard'),
    ])),

    # REST API routs
    path('api/', include(router.urls)),  # ViewSet covers all friend request operations
]