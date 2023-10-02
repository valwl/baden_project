from django.db import models
#from baden_baden.locate.models import Location
from django.contrib.auth import get_user_model

User = get_user_model()


class Apartment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    apartments_type = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    #locate = models.ForeignKey(Location, on_delete=models.CASCADE)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    guests = models.PositiveIntegerField()
    max_guests = models.PositiveIntegerField()

    def __str__(self):
        return f'<Title: {self.title}>\t<id: {self.pk}>'


class ApartmentPrice(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    weekend_price = models.DecimalField(max_digits=10, decimal_places=2)
    holiday_price = models.DecimalField(max_digits=10, decimal_places=2)
    additional_guest_price = models.DecimalField(max_digits=10, decimal_places=2)
    under_14 = models.DecimalField(max_digits=10, decimal_places=2)
    under_4 = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'<apartment id: {self.apartment.pk}> <base price: {self.base_price}>'


class ApartmentImage(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='apartments/img')


class Review(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()


class ReviewImage(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='apartments/img/reviews')
