from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_apartments_list, name='apartments_list'),
    path('apartment_instance/<int:pk>/', views.get_apartment_instance, name='apartments_instance'),
    path('apartment_create', views.create_apartment, name='create_apartment'),
]