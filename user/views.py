from django.urls import reverse
import requests, json
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from user.models import Rating
from api.views import get_book

# Create your views here.
@login_required(login_url='/auth/login/')
def user_profile(request, username):
    user_profile = User.objects.get(username=username)
    top5ratings = [
        {"rating": book.rating, "json_data": json.loads(get_book(request, book.book_id).content)['volumeInfo']} for book in Rating.objects.filter(user=user_profile).order_by('-rating')[:5]
    ]
    context = {
        "user_profile": user_profile,
        "top5ratings": top5ratings
    }

    return render(request, 'profile.html', context)

@login_required(login_url='/auth/login/')
def become_curator(request):
    user = request.user
    user.profile.is_curator = True
    user.profile.save()

    return JsonResponse({"is_curator": user.profile.is_curator})