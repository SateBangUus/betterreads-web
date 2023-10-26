from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from book.models import Item
# Create your views here.
@login_required(login_url='/login')
def incrementBook(request, id):
    data = Item.objects.get(id =id)
    data.amount +=1
    data.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def decrementBook(request, id):
    data = Item.objects.get(id =id)
    data.amount -=1
    data.save()
    return HttpResponseRedirect(reverse('main:show_main'))
def buy_book(request):#id):
    #data = Item.objects.get(id =id)
    #books = data.amount
    #context = {'books': books}
    return render(request, "buy_product.html")