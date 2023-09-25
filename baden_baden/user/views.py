from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from . forms import CustomUserCreationForm
from . models import Profile


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            return redirect('login')
    form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, 'user/register.html', context)


@login_required
def profile_view(request):
    profile = Profile.objects.get(user=request.user)
    context = {'profile': profile}
    return render(request, 'user/profile.html', context)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print(user)
            if user:
                login(request, user)
                return redirect('profile')
    form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'user/login.html', context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
