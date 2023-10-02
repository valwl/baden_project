from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, get_user_model, update_session_auth_hash
from . models import CustomUser
from django.core.exceptions import ValidationError
from . custom_auth import AuthBackend
User = get_user_model()


def validation_phone_number(phone_number):
    digits = ''.join(filter(str.isdigit, phone_number))
    if 10 > len(digits) > 11:
        raise ValidationError('Phone number must be 10 or 11 digits long.')
    return phone_number


class CustomUserCreationForm(UserCreationForm):
    login = forms.CharField(max_length=255, label='email or phone_number')
    class Meta:
        model = CustomUser
        fields = ['login', 'first_name', 'last_name']

    def clean_login(self):
        login = self.cleaned_data.get('login')
        if '@' not in login:
            return validation_phone_number(login)
        else:
            return self.cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = None
        user.phone_number = None
        login = self.cleaned_data.get('login')
        if validation_phone_number(login):
            user.phone_number = login
        else:
            user.email = login
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
        fields = ['phone_number', 'email', 'first_name', 'last_name']


class LoginForm(forms.Form):
    login = forms.CharField(max_length=255, label='email or phone_number')
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)

    def clean(self):
        login_data = self.cleaned_data.get('login')

        if '@' not in login_data:
            validation_phone_number(self.cleaned_data.get('login'))
            return self.cleaned_data


class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User

















