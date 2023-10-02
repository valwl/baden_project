from django.shortcuts import render, redirect
from . models import Reservation, Apartment
from . forms import BookingForm


def book_apartment(request, pk):
    apartment = Apartment.objects.get(pk=pk)

    if request.method == 'POST':
        form = BookingForm(data=request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.apartment = apartment
            reservation.total_price = calculate_total_price()
            reservation.save()
            return redirect('success booking')
    form = BookingForm()
    context = {'form': form}
    return render(request, 'booking/book_apartment.html', context)


