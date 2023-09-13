from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_apartments_list, name='apartments_list')
]