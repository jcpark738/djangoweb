from django.contrib import admin
from django.urls import path
from .views import *
# from . import views

urlpatterns = [
    path('', index),
    # path('', views.index, name='index'),
    path('program/',program),
]