from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from . models import CustomUser
from django.core.exceptions import ValidationError


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'phone_number', 'first_name', 'last_name']

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        digits = ''.join(filter(str.isdigit, phone_number))
        if len(digits) < 10 and len(digits) > 11:
            raise forms.ValidationError('Phone number must be 10 or 11 digits long.')
        return phone_number

    def save(self, commit=True):
        user = super().save(commit=False)
        # Вызываем create_user вашего кастомного менеджера
        user = CustomUser.objects.create_user(
            email=user.email,
            phone_number=user.phone_number,
            password=self.cleaned_data['password1']
        )
        if commit:
            user.save()
        return user


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = '__all__'


class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = '__all__'

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username:
            if '@' in username:
                user = CustomUser.objects.get(email=username)
                if user is not None:
                    return user.email
            else:
                user = CustomUser.objects.get(phone_number=username)
                if user is not None:
                    return user.phone_number
        raise ValidationError('user with this email or phone_number not found')




