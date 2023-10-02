from django.db import models


class Location(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    map = models.TextField()
    characteristics = models.TextField()

    def __str__(self):
        return f'{self.title}, {self.pk}'
