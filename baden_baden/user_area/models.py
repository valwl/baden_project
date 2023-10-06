from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='user/img', default='user/img/149017.png')

    def __str__(self):
        return f'profile of {self.user.email if self.user.email else self.user.phone_number}'

