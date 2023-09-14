from django.shortcuts import render
from .models import Apartment


def get_apartments_list(request):
    apartments = Apartment.objects.all()

    return render(request, 'apartaments/apartments_list.html', {'apartments': apartments})
