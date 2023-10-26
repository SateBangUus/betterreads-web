from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/auth/login/')
def user_profile(request):
    return render(request, 'profile.html')

@login_required(login_url='/auth/login/')
def become_curator(request):
    user = request.user
    user.profile.is_curator = True
    user.profile.save()
    return JsonResponse({"is_curator": user.profile.is_curator})