from django import forms
from . models import Reservation


class BookingForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['check_in_date', 'check_out_date']
