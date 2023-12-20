from django.urls import path, include
from main.views import show_main, search_books, search_books_blank, search_books_flutter
from book.views import book_detail

app_name = 'main'
urlpatterns = [
    path('', show_main, name='show_main'),
    path('search-books/', search_books, name='search_books'),
    path('search-books-blank/', search_books_blank, name='search_books'),
    path('book-detail/<int:book_id>/', book_detail, name='book_detail'),
    path('search-book-flutter/', search_books_flutter, name='search_book_flutter'),
]
