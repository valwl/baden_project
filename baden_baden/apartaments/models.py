from django.db import models


class Apartments(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    ct = {
        'ST': 'standart',
        'MD': 'medium',
        'LX': 'lux'
    }

    #category = models.CharField(max_length=5, choices=ct, default=ct['MD'])





    def __str__(self):
        return f'{ self.title } id:{self.pk}'


class ApartmentImages(models.Model):
    image = models.ImageField(upload_to='apartment')
    apartment = models.ForeignKey(Apartments, on_delete=models.CASCADE)


class Characters(models.Model):
    rooms = models.ImageField()
    persone = models.IntegerField()
