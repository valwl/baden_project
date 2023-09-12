from django.db import models



class Hotel(models.Model):
    name = models.CharField(max_length=255)
    star_rating = models.PositiveIntegerField()
    locations = models.CharField(max_length=255)
    descriptions = models.TextField()
    check_in_time = models.TimeField()
    check_out_time = models.TimeField()


class HotelImg(models.Model):
    img = models.ImageField()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)


class RoomType(models.Model):
   hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
   type_name = models.CharField(max_length=255)

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    type_name = models.CharField(max_length=255)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(RoomType, on_delete=models.CASCADE)

class RoomImage(models.Model):
    img = models.ImageField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)


class RoomPrice(models.Model):
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    weekend_price = models.DecimalField(max_digits=10, decimal_places=2)
    holiday_price = models.DecimalField(max_digits=10, decimal_places=2)
    extra_guest = models.DecimalField(max_digits=10, decimal_places=2)
    room = models.OneToOneField(Room, on_delete=models.CASCADE)


class Sales(models.Model):
    birthday = models.IntegerField()
    long_term_rental = models.IntegerField()
    room = models.ForeignKey(RoomPrice, on_delete=models.CASCADE)


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    guest = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f' Booking {self.id}- {self.user.username}'


class Review(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    star = models.PositiveIntegerField()
    text = models.TextField()





