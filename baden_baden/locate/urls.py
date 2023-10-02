from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.list_view, name='index'),
    path('detail/<int:pk>/', views.detail, name='detail'),
]