from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from user.models import Curator

# Create your views here.
def login_user(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/user/profile/')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')

def register_user(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            Curator.objects.create(user=user)
            messages.success(request, 'Account created successfully')
            return HttpResponseRedirect('/')
    context = {'form': form}
    return render(request, 'register.html', context)

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/auth/login/')
