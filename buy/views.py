# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from buy.models import Cart
from book.models import Book
from django.http import HttpResponse
from django.core import serializers
# Create your views here.
@login_required(login_url='/login')
def incrementBook(request, id):
    data = Cart.objects.get(id =id)
    data.amount +=1
    data.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def decrementBook(request, id):
    data = Cart.objects.get(id =id)
    data.amount -=1
    data.save()
    return HttpResponseRedirect(reverse('main:show_main'))
def buy_book(request):#id):
    #data = Item.objects.get(id =id)
    #books = data.amount
    #context = {'books': books}
    return render(request, "buy_product.html")
def cart(request):
    data = Cart.objects.filter(user=request.user)
    context = {"data" : data,}
    return render(request, "buy.html",context)
def get_product_json(request):
    book_item = Cart.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', book_item))