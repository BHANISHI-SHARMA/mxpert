from django.contrib.auth.models import User
from django.db import models
from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_request, name='login'),
    path('signup/', views.register_request, name='register'),

]