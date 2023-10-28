# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from buy.models import Cart
from book.models import Book
from django.http import HttpResponse
from django.core import serializers
import json
# Create your views here.
@login_required(login_url='/login')
def incrementBook(request, id):
    data = Cart.objects.get(pk =id)
    data.amount +=1
    data.save()
    return HttpResponse(b"Increment",201)

def decrementBook(request, id):
    data = Cart.objects.get(pk =id)
    data.amount -=1
    data.save()
    return HttpResponse(b"Decrement",201)
def buy_book(request):#id):
    #data = Item.objects.get(id =id)
    #books = data.amount
    #context = {'books': books}
    return render(request, "buy_product.html")
def cart(request):
    data = Cart.objects.filter(user=request.user)
    counter = len(data)
    context = {"data" : data,
               "counter": counter}
    return render(request, "buy.html",context)
def get_product_json(request):
    book_item = Cart.objects.filter(user=request.user)
    temp = []
    for book in book_item:
        temp.append({
            "title" : book.book.title,
            "author" : book.book.author,
            "publisher" : book.book.publisher,
            "published_date" : book.book.published_date,
            "description" : book.book.description,
            "genre" : book.book.genre,
            "image" : book.book.image_link,
        })
    finaljson = json.dumps(temp)
    return HttpResponse(finaljson, content_type='application/json')
def delete_book(request,id):
    data = Cart.objects.get(pk=id)
    data.delete()
    return HttpResponse(b"Deleted",201)