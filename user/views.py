from django.urls import reverse
import requests, json
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count
from book.models import Review

# Create your views here.
@login_required(login_url='/auth/login')
def user_profile(request, username=""):
    try:
        user_profile = User.objects.get(username=username)
    except User.DoesNotExist:
        if username == "":
            user_profile = request.user
        else:
            return render(request, 'profile_404.html')

    try:
        reviews = [
            {"rating": review.rating, "book": review.book} for review in Review.objects.filter(user=user_profile).order_by('-rating')[:5]
        ]
        total_review = Review.objects.filter(user=user_profile).count()
        average_rating = round(Review.objects.filter(user=user_profile).aggregate(Avg('rating'))['rating__avg'], 2)
        fav_genre = Review.objects.filter(user=user_profile).values('book__genre').annotate(genre_total=Count('book__genre')).order_by('-genre_total')
    except:
        reviews = []
        total_review = 0
        average_rating = 0
        fav_genre = []

    context = {
        "user_profile": user_profile,
        "join_date": user_profile.date_joined.strftime("%B %Y"),
        "top_reviews": reviews,
        "total_reviews": total_review,
        "average_rating": average_rating,
        "fav_genres": fav_genre
    }

    return render(request, 'profile.html', context)

@login_required(login_url='/auth/login')
def become_curator(request):
    user = request.user
    user.profile.is_curator = False if user.profile.is_curator else True
    user.profile.save()

    return HttpResponseRedirect(reverse('user:user_profile'))

