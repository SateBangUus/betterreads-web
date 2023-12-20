from django.urls import path
from . import views


app_name = 'book'
urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('<int:book_id>/', views.book_detail, name='book_detail'),
    path('<int:book_id>/add_reviews', views.add_review, name='add_review'),
    #path('curator-section/', views.curator_section, name='curator_section'),
    path('<int:book_id>/get-reviews/', views.get_reviews, name='get_reviews'),
    path('<int:book_id>/delete_review/', views.delete_review, name='delete_review'),
    path('<int:book_id>/add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('json/<int:book_id>/', views.get_book_json, name='get_book_json'),
    path('json/all/', views.get_all_books_json, name='get_all_books_json'),
    path('json/user/<int:user_id>/', views.get_user_books_json, name='get_user_books_json'),
    path('reviews/json/<int:book_id>/', views.get_book_reviews, name='book_reviews'),




]
