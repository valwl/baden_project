from django.db import models
from django.contrib.auth.models import User


class Hotel(models.Model):
    name = models.CharField(max_length=255)
    star_rating = models.PositiveIntegerField()
    locations = models.CharField(max_length=255)
    descriptions = models.TextField()


class HotelImg(models.Model):
    img = models.ImageField()


class RoomType(models.Model):
    category = models.CharField(max_length=25)
    base_guest = models.PositiveIntegerField()
    max_guest = models.PositiveIntegerField()
    rooms_number = models.PositiveIntegerField()


class RoomImage(models.Model):
    img = models.ImageField()


class Meal(models.Model):
    title = models.CharField(max_length=125)
    description = models.TextField()
    price = models.PositiveIntegerField()


class Host(models.Model):
    img = models.ImageField()
    phone = models.CharField(max_length=17)
    name = models.CharField(max_length=125)


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    type_name = models.CharField(max_length=255)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    host = models.ForeignKey(Host, on_delete=models.CASCADE)


class RoomPrice(models.Model):
    base_price = models.IntegerField()
    weekend_price = models.IntegerField()
    holiday_price = models.IntegerField()
    extra_guest = models.PositiveIntegerField()
    room = models.OneToOneField(Room, on_delete=models.CASCADE)


class Sales(models.Model):
    birthday = models.IntegerField()
    long_term_rental = models.IntegerField()
    room = models.ForeignKey(RoomPrice, on_delete=models.CASCADE)


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    apartment = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f' Booking {self.id}- {self.user.username}'


class Review(models.Model):
    star = models.PositiveIntegerField()
    review = models.TextField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)




