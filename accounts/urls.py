from django.contrib import admin
from django.urls import path, include
import accounts.views


urlpatterns = [
    path('', accounts.views.profile, name= 'profile')
]