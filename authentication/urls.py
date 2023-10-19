<<<<<<< HEAD
from authentication.views import login_user, register_user
=======
from authentication.views import login_user, register_user, logout_user
>>>>>>> f86f652 (add logout)
from django.urls import path

app_name = 'authentication'
urlpatterns = [
    path('login/', login_user, name='login'),
    path('register/', register_user, name='register'),
<<<<<<< HEAD
=======
    path('logout/', logout_user, name='logout')
>>>>>>> f86f652 (add logout)
]