from api.views import login, register, logout, user_stats, profile
from django.urls import path

app_name = 'api'
urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('user/', profile, name='profile'),
    path('user/stats/', user_stats, name='user_stats'),
]