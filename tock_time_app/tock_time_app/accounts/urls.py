from django.urls import path, include

from tock_time_app.accounts import views

urlpatterns = [
    path('register/', views.AppUserRegisterView.as_view(), name='register'),
    path('login/', views.AppUserLogInView.as_view(), name='login'),
    path('logout/', views.AppUserLogOutView.as_view(), name='logout'),
    path('profile/', include([
        path('<int:pk>/', include([
            path('', views.ProfileDetailsView.as_view(), name='profile-details'),
            path('edit/', views.ProfileEditView.as_view(), name='profile-edit'),
            path('delete/', views.ProfileDeleteView.as_view(), name='profile-delete'),
        ])),
        path('deleted/', views.ProfileDeletedPageView.as_view(), name='profile-deleted-page'),
    ])),
]
