from django.urls import path
from user.views import user_profile, become_curator

app_name = 'user'
urlpatterns = [
    path('curator', become_curator, name='become_curator'),
    path('profile/', user_profile, name='user_profile'),
    path('profile/<str:username>', user_profile, name='user_profile'),
]