from django.shortcuts import render
from firstapp.forms import UserForm, UserProfileInfoForm
# Create your views here.

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout


def homepage(request):
    dec ={'text': "hello world hello mohamed Hello"}
    return render(request, 'firstapp/homepage.html', context=dec)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))

@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")

def index(request):
    dec={}
    return render(request, 'firstapp/index.html', context = dec)


def other(request):
    dec={}
    return render(request, 'firstapp/other.html', context=dec)


def relative(request):
    dec={}
    return render(request, 'firstapp/relativehtml.html', context=dec)

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileInfoForm(data =request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered =True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm
        profile_form = UserProfileInfoForm

    return render(request, 'firstapp/registeration.html',{'user_form':user_form, 'profile_form':profile_form,'registered':registered} )




def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('homepage'))

            else:
                return HttpResponse("Account Not Active! ")
        else:
            print("Someone Tried to login and failed! ")
            print(f"UserName: {username} and Password: {password}")
            return HttpResponse ("invalid login detailes supplied!")

    else:
        return render(request, 'firstapp/login.html', {})

