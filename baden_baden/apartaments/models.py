from django.db import models



class Apartment(models.Model):
    # user = models.ForeignKey()
    title = models.CharField(max_length=100)
    apartments_type = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    description = models.TextField()

    guests = models.PositiveIntegerField()
    max_guests = models.PositiveIntegerField()

    def __str__(self):
        return f'<Title: {self.title}>\t<id: {self.pk}>'


class ApartmentPrice(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    additional_guest_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'<apartment id: {self.apartment.pk}> <base price: {self.base_price}>'


class ApartmentImage(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='###')


class Booking(models.Model):
    # user = models.ForeignKey()
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    guest_count = models.PositiveIntegerField()


class Review(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    # user = models.ForeignKey()
    rating = models.PositiveIntegerField()
    comment = models.TextField()


class ReviewImage(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='###')

