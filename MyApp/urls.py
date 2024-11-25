from django.contrib import admin
from django.urls import path
from MyApp.views import *

urlpatterns = [
    path('', index),
]
