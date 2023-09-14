from django.shortcuts import render
from . models import Apartments


def index(request):
#   apartment = Apartments.objects.all()
 #   context = {'apartment': apartment}
    return render(request, 'apartaments/apartments_list.html')


