from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count
from book.models import Review

# Create your views here.
@login_required(login_url='/auth/login/')
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

@login_required(login_url='/auth/login/')
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        username = request.POST.get('username', '')
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')

        if username == '':
            messages.error(request, "Username cannot be empty")
            return render(request, 'edit.html', {'user': user})
        if user.username != username:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists")
                return render(request, 'edit.html', {'user': user})
        if email != '' and user.email != email:
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already exists")
                return render(request, 'edit.html', {'user': user})
        
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email

        user.save()
        return HttpResponseRedirect(reverse('user:user_profile'))
    return render(request, 'edit.html', {'user': user})

@login_required(login_url='/auth/login')
def become_curator(request):
    user = request.user
    user.profile.is_curator = False if user.profile.is_curator else True
    user.profile.save()

    return HttpResponseRedirect(reverse('user:user_profile'))

