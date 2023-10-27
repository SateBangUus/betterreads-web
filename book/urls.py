from django.urls import path
from . import views

app_name = 'book'
urlpatterns = [
    path('book-list/', views.book_list, name='book_list'),
    path('book-detail/<int:book_id>/', views.book_detail, name='book_detail'),
    path('add-review/<int:book_id>/', views.add_review, name='add_review'),
    path('curator-section/', views.curator_section, name='curator_section'),
    path('fetch-books-from-google-books-api/', views.fetch_books_from_google_books_api, name='fetch_books_from_google_books_api'),

]
