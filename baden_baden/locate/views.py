from django.shortcuts import render
from . models import Location


def list_view(request):
    locate = Location.objects.all()
    context = {'locate': locate}
    return render(request, 'locate/index.html', context)


def detail(request, pk):
    locate = Location.objects.get(pk=pk)
    context = {'locate': locate}
    return render(request, 'locate/detail.html', context)

