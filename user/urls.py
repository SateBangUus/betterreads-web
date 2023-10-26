from django.urls import path
from user.views import user_profile, become_curator

app_name = 'user'
urlpatterns = [
    path('profile/', user_profile, name='profile'),
    path('curator/', become_curator, name='become_curator')
]