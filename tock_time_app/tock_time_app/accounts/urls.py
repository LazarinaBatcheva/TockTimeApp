from django.urls import path
from tock_time_app.accounts import views

urlpatterns = [
    path('register/', views.AppUserRegisterView.as_view(), name='register'),
    path('login/', views.AppUserLogInView.as_view(), name='login'),
    path('logout/', views.AppUserLogOutView.as_view(), name='logout'),
]