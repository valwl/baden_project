from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . models import Profile


@login_required
def profile_view(request):
    profile = Profile.objects.get(user=request.user)
    context = {'profile': profile}
    return render(request, 'user/profile.html', context)




