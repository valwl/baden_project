from django.db import models
from apartaments.models import Apartment, ApartmentPrice
from datetime import timedelta
from django.contrib.auth import get_user_model

User = get_user_model()


class Booking(models.Model):
    CREATED = 1
    PAID = 2
    CHECK_IN = 3
    CHECK_OUT = 4
    STATUSES = (
        (CREATED, 'бронирование создано'),
        (PAID, 'оплачено'),
        (CHECK_IN, 'заселение'),
        (CHECK_OUT, 'выселение'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    status = models.SmallIntegerField(default=CREATED, choices=STATUSES)
    #total_price = models.DecimalField(max_digits=10, decimal_places=2, default=)
    price = models.ForeignKey(ApartmentPrice, on_delete=models.CASCADE)
    guest_count = models.PositiveIntegerField()
    created_time = models.DateTimeField(auto_now_add=True)

    def calculate_total_price(self):
        duration = self.check_out_date - self.check_in_date
        if duration.days < 1:
            raise ValueError('Booking have to be longer at one day ')
        total_price = self.price.base_price * duration.days
        return total_price

    def __str__(self):
        return f'reservation for {self.user.first_name}, {self.apartment.title}'




# class Booking(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
#     check_in_date = models.DateField()
#     check_out_date = models.DateField()
#     guest_count = models.PositiveIntegerField()

