from users.models import Profile
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm
from pic.models import Picture


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('users/home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):

    current_user = request.user
    myPics = Picture.objects.filter(user = current_user)

    profile_user = Profile.objects.get(user = current_user )

    context = {

        'user' : profile_user,
        'pics' : myPics

    }


    return render(request,'users/profile.html',context)
   


    