from django.urls import path
from user.views import user_profile

app_name = 'user'
urlpatterns = [
    path('profile/', user_profile, name='profile')
]