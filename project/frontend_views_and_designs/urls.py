from django.contrib import admin
from django.urls import path

from .views import LandingPage

urlpatterns = [
    path("", LandingPage)
]
