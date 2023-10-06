from django.shortcuts import render, redirect
from .models import Apartment, ApartmentPrice
from . forms import CreateApartmentForm, apartment_price_form_set, apartment_image_form_set
from django.contrib.auth.decorators import login_required
from booking.forms import BookingForm
from django.contrib import messages

def get_apartments_list(request):
    apartments = Apartment.objects.all()
    return render(request, 'apartments/apartments_list.html', {'apartments': apartments})


def get_apartment_instance(request, pk):
    instance_apartment = Apartment.objects.get(pk=pk)
    form = BookingForm()
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = BookingForm(data=request.POST)
            if form.is_valid():
                price = ApartmentPrice.objects.get(apartment=pk)
                reservation = form.save(commit=False)
                reservation.user = request.user
                reservation.apartment = instance_apartment
                reservation.price = price
                reservation.save()
                messages.success(request, 'booking is success')
                return redirect('profile')
    context = {'apartment': instance_apartment,
               'form': form
               }
    return render(request, 'apartments/apartment_instance.html', context)


@login_required
def create_apartment(request):
    if request.method == 'POST':
        apartment_form = CreateApartmentForm(data=request.POST)
        price_form_set = apartment_price_form_set(request.POST, prefix='price')
        img_form_set = apartment_image_form_set(request.POST, request.FILES, prefix='img')
        if apartment_form.is_valid() and price_form_set.is_valid() and img_form_set.is_valid():
            apartment = apartment_form.save(commit=False)
            apartment.user = request.user
            apartment.save()
            price_form_set.instance = apartment
            price_form_set.save()
            img_form_set.instance = apartment
            img_form_set.save()
            return redirect('apartments_list')

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




