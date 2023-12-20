from api.views import login, register, logout, profile
from django.urls import path

app_name = 'api'
urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('user/<str:username>/', profile, name='profile'),
]