from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def show_main(request):
    if request.user.is_authenticated:
        return render(request, 'main.html')
    return HttpResponseRedirect('/auth/login/')