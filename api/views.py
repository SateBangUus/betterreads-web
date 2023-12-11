import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Avg, Count
from django.core import serializers

from book.models import Review
from django.contrib.auth.models import User

# Create your views here.
@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(request.POST)
        user = authenticate(
            username=username,
            password=password
        )

        if user is not None:
            auth_login(request, user)
            return JsonResponse({
                'username': user.username,
                'message': 'Success',
                'status': True,
            }, status=200)
        else:
            return JsonResponse({
                'message': 'Failed',
                'status': False,
            }, status=401)

@csrf_exempt    
def logout(request):
    username = request.user.username

    try:
        auth_logout(request)
        return JsonResponse({
            'username': username,
            'message': 'Success',
            'status': True,
        }, status=200)
    except:
        return JsonResponse({
            'message': 'Failed',
            'status': False,
        }, status=401)

@csrf_exempt
def register(request):
    if request.method == "POST":
        data = json.loads(request.body)
        form = UserCreationForm({"username": data['username'], "password1": data['password1'], "password2": data['password2']})
        if form.is_valid():
            form.save()
            return JsonResponse({
                "status": True,
                "message": "User successfully registered!"
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Register failed!",
            }, status=401)
        
@csrf_exempt
def profile(request):
    if request.method == "GET":
        user = request.user

        return JsonResponse({
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "is_curator": user.profile.is_curator,
        }, status=200)
    
    elif request.method == "POST":
        user = request.user
        data = json.loads(request.body)

        if data['username'] != user.username:
            if User.objects.filter(username=data['username']).exists():
                return JsonResponse({
                    "status": False,
                    "message": "Username already exists!"
                }, status=401)
        if data['email'] != user.email:
            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({
                    "status": False,
                    "message": "Email already exists!"
                }, status=401)

        user.username = data['username']
        user.email = data['email']
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.save()

        return JsonResponse({
            "status": True,
            "message": "Profile successfully updated!"
        }, status=200)

@csrf_exempt
def user_stats(request):
    if request.method == "GET":
        user = request.user

        reviews = [
            {"rating": review.rating, "book": serializers.serialize("json", [review.book,])} for review in Review.objects.filter(user=user).order_by('-rating')[:5]
        ]
        total_review = Review.objects.filter(user=user).count()
        average_rating = round(Review.objects.filter(user=user).aggregate(Avg('rating'))['rating__avg'], 2)
        fav_genre = list(Review.objects.filter(user=user).values('book__genre').annotate(genre_total=Count('book__genre')).order_by('-genre_total'))

        context = {
            "join_date": user.date_joined.strftime("%B %Y"),
            "top_reviews": reviews,
            "total_reviewsl": total_review,
            "average_rating": average_rating,
            "fav_genres": fav_genre
        }

        return JsonResponse(context, status=200)