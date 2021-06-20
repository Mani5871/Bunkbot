from django.contrib import admin
from django.urls import path, include
from . import views
from . import codetantra

urlpatterns = [
    path('', views.index, name = 'index'),
    path('signup', views.signup, name = 'signup'),
    path('register', views.register, name = 'register'),
    path('login', views.login, name = 'login'),
    path('logout', views.logout, name = 'logout'),
    path('attend', codetantra.attend, name = 'attend')
]
