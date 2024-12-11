"""
URL configuration for the common app.
This module defines the routing for the common application, including the home page view.
"""

from django.urls import path
from tock_time_app.common import views

urlpatterns = [
    # Home page route
    path('', views.HomePageView.as_view(), name='home'),
]