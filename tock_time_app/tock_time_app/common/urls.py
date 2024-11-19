from django.urls import path
from tock_time_app.common import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
]