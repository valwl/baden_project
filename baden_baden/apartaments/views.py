from django.shortcuts import render, redirect
from .models import Apartment
from . forms import CreateApartmentForm, apartment_price_form_set, apartment_image_form_set
from django.contrib.auth.decorators import login_required


def get_apartments_list(request):
    apartments = Apartment.objects.all()
    return render(request, 'apartments/apartments_list.html', {'apartments': apartments})


def get_apartment_instance(request, pk):
    instance_apartment = Apartment.objects.get(pk=pk)
    return render(request, 'apartments/apartment_instance.html', {'apartment': instance_apartment})


@login_required
def create_apartment(request):
    if request.method == 'POST':
        data = {}
        data += request.POST
        data.update({'user': request.user})
        print(data)
        apartment_form = CreateApartmentForm(data=request.POST)
        price_form_set = apartment_price_form_set(request.POST, prefix='price')
        img_form_set = apartment_image_form_set(request.POST, request.FILES, prefix='img')
        if apartment_form.is_valid() and price_form_set.is_valid() and img_form_set.is_valid:
            apartment = apartment_form.save(commit=False)
            apartment.user = request.user
            apartment.save()
            price_form_set.instance = apartment
            price_form_set.save()
            img_form_set.instance = apartment
            img_form_set.save()
            return redirect('apartment_list')
    else:
        apartment_form = CreateApartmentForm()
        price_form_set = apartment_price_form_set( prefix='price')
        img_form_set = apartment_image_form_set( prefix='img')
        context = {
            'apartment_form': apartment_form,
            'price_form_set': price_form_set,
            'img_form_set': img_form_set,
        }
        return render(request, 'apartments/create_apartment.html', context)



# @login_required
# def update_apartment(request):
#     if request.method == 'POST':
#         form = UpdateForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('success_page')
#     form = UpdateForm()
#     context = {'form': form}
#     return render(request, '', context)


@login_required
def delete_apartment(request, pk):
    if request.method == 'POST':
        apartment = Apartment.objects.get(pk=pk)
        apartment.delete()
        return redirect('apartments/apartments_list.html')
    return render('apartments/delete.html')




