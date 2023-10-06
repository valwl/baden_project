from django import forms
from .models import Apartment, ApartmentPrice, ApartmentImage
from django.forms import inlineformset_factory


class CreateApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = ['title', 'description', 'address', 'max_guests', 'guests', 'apartments_type']


class UpdateApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = ['title', 'description', 'address', 'max_guests', 'guests', 'apartments_type']


class PriceForm(forms.ModelForm):
    class Meta:
        model = ApartmentPrice
        fields = ['base_price', 'weekend_price', 'holiday_price', 'additional_guest_price', 'under_14', 'under_4']


class ImgForm(forms.ModelForm):
    class Meta:
        model = ApartmentImage
        fields = ['img']


apartment_price_form_set = inlineformset_factory(Apartment, ApartmentPrice, form=PriceForm, extra=1)
apartment_image_form_set = inlineformset_factory(Apartment, ApartmentImage, form=ImgForm, extra=1)

