from django.contrib import admin
from django.contrib.auth import get_user_model
from . models import Profile

admin.site.register(Profile)
user = get_user_model()
admin.site.register(user)
