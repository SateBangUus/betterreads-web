from django.urls import path
from buy.views import incrementBook, decrementBook, buy_book, cart, get_product_json
app_name = 'buy'
urlpatterns = [
    path('increment/<int:id>', incrementBook, name='increment'),
    path('decrement/<int:id>', decrementBook, name='decrement'),
    path('buy-book/', buy_book, name='buy_book'),
    path('buy/', cart, name='cart'),
    path('get-product/', get_product_json, name='get_product_json'),
]