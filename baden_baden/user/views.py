from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, update_session_auth_hash
from . forms import CustomUserCreationForm, LoginForm, CustomPasswordChangeForm, CustomUserChangeForm
from user_area.models import Profile
from . custom_auth import AuthBackend
from django.contrib import messages
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            try:
                user = form.save()
                Profile.objects.create(user=user)
            except IntegrityError:
                form.add_error('login', ValidationError('user with this login already exists'))
                return render(request, 'users/register.html', {'form': form})
            return redirect('login')

    form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, 'user/register.html', context)




def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('login')
            password = form.cleaned_data.get('password')

            user = AuthBackend().authenticate(request, login=username, password=password)
            if user:
                login(request, user)
                return redirect('profile')
            else:
                form.add_error('login', ValidationError('incorrect login or password'))
                return render(request, 'user/login.html', {'form': form})
    form = LoginForm()
    context = {'form': form}
    return render(request, 'user/login.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')




def past_booking(request):
    pass


@login_required
def settings(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    form = CustomUserChangeForm()
    context = {'form': form}
    return render(request, 'user/settings.html', context)


@login_required
def password_change(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.post)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'password change is success')
            return redirect('profile')
        else:
            messages.error(request, 'error in form')
    form = CustomPasswordChangeForm(request.user)
    context = {'form': form}
    return render(request, 'users/change_password.html', context)


