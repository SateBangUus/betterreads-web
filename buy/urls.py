from django.urls import path
from buy.views import incrementBook, decrementBook, buy_book
app_name = 'buy'
urlpatterns = [
    path('increment/<int:id>', incrementBook, name='increment'),
    path('decrement/<int:id>', decrementBook, name='decrement'),
    path('buy-book/', buy_book, name='buy_book'),
]