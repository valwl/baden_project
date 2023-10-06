from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect

urlpatterns = [
    path('register/', views.register, name='register'),
    #path('login/', LoginView.as_view(template_name='user/login.html', ), name='login'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('settings/', views.settings, name='settings'),
]