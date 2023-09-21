from django.shortcuts import render
from .models import Apartment


def get_apartments_list(request):
    apartments = Apartment.objects.all()

    return render(request, 'apartments/apartments_list.html', {'apartments': apartments})


def get_apartment_instance(request, pk):
    instance_apartment = Apartment.objects.get(pk=pk)
    return render(request, 'apartments/apartment_instance.html', {'apartment': instance_apartment})
