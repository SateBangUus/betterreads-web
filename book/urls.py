from django.urls import path
from book.views import incrementBook, decrementBook, buy_book
app_name = 'book'
urlpatterns = [
    path('increment/<int:id>', incrementBook, name='increment'),
    path('decrement/<int:id>', decrementBook, name='decrement'),
    path('buy-book/', buy_book, name='buy'),
]