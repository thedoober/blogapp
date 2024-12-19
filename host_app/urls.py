from django.contrib import admin
from django.urls import path, include
from host_app import views


urlpatterns = [
    path('', views.index, name='home'),
    
]