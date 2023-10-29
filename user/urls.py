from django.urls import path
from user.views import user_profile, become_curator, edit_profile

app_name = 'user'
urlpatterns = [
    path('curator', become_curator, name='become_curator'),
    path('profile/', user_profile, name='user_profile'),
    path('profile/edit', edit_profile, name='edit_profile'),
    path('profile/<str:username>', user_profile, name='user_profile'),
]