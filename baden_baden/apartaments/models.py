from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=255)
    star_rating = models.PositiveIntegerField()
    locations = models.CharField(max_length=255)
    descriptions = models.TextField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=17, null=True, blank=True)

class HotelImg(models.Model):
    pass


class RoomType(models.Model):
    pass


class RoomImage(models.Model):
    pass


class Meal(models.Model):
    pass


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    type_name = models.CharField(max_length=255)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)


class RoomPrice(models.Model):
    pass


class Booking(models.Model):
    pass


class Review(models.Model):
    pass
