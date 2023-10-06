from django.shortcuts import render, redirect
from . models import Booking, Apartment
from . forms import BookingForm
import stripe
stripe.api_key = 'sk_test_51NwzRzEoF28QzXkJSX5tamYjXlJ1qyey0Z8El4Guks0O0Rep5lCqRC5A7lJfWeZVHIQSf6DiOoXy7W2KxMFpKdmS00w1NV1MJ8'

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



def form_valid(self, form):
    form.instance.initiatior = self.request.user
    return super(book_apartment(), self).form_valid(form)

