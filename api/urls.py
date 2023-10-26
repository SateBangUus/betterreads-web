from django.urls import path
from api.views import get_books_by_title, get_book_by_isbn, get_books_by_author, get_books_by_genre, get_book, get_id_by_isbn

app_name = 'api'
urlpatterns = [
    path('get_book', get_book, name='get_book'),
    path('get_books_by_title', get_books_by_title, name='get_books_by_title'),
    path('get_book_by_isbn', get_book_by_isbn, name='get_book_by_isbn'),
    path('get_books_by_author', get_books_by_author, name='get_books_by_author'),
    path('get_books_by_genre', get_books_by_genre, name='get_books_by_genre'),
    path('get_id_by_isbn', get_id_by_isbn, name='get_id_by_isbn'),
]