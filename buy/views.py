# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from buy.models import Cart
from book.models import Book
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@login_required(login_url='/login')
def cart(request):
    data = Cart.objects.filter(user=request.user)
    counter = len(data)
    context = {"data" : data,
               "counter": counter}
    return render(request, "buy.html",context)
@csrf_exempt
def incrementBook(request, id):
    data = Cart.objects.get(pk =id)
    data.amount +=1
    data.save()
    return HttpResponseRedirect(reverse('buy:cart'))
@csrf_exempt
def decrementBook(request, id):
    data = Cart.objects.get(pk =id)
    data.amount -=1
    data.save()
    return HttpResponseRedirect(reverse('buy:cart'))
def buy_book(request):
    data = Cart.objects.filter(user=request.user).all()
    data.delete()
    return render(request, "buy_product.html")
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
            "amount" : book.amount,
            "id" : book.id,
        })
    finaljson = json.dumps(temp)
    return HttpResponse(finaljson, content_type='application/json')

def get_product_flutter(request):
    if not request.user.is_authenticated:
        return JsonResponse({"error": "User is not authenticated"}, status=403)
    book_item = Cart.objects.filter(user=request.user)
    temp = []
    for book in book_item:
        temp.append({
            "title" : book.book.title,
            "author" : book.book.author,
            "image" : book.book.image_link,
            "amount" : book.amount,
            "id" : book.id,
        })
    finaljson = json.dumps(temp)
    return HttpResponse(finaljson, content_type='application/json')
@csrf_exempt
def incrementBookFlutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)

        book = Cart.objects.get(pk=data['id'])
        book.amount += 1
        book.save()

        return JsonResponse({"status": "success"}, status=200)
@csrf_exempt
def decrementBookFlutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)

        book = Cart.objects.get(pk=data['id'])
        if (book.amount > 1):
            book.amount -= 1
            book.save()

        return JsonResponse({"status": "success"}, status=200)
def deleteBookFlutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        book = Cart.objects.get(pk=data['id'])
        book.delete()

        return JsonResponse({"status": "success"}, status=200)

@csrf_exempt
def submitflutter(request):
    data = Cart.objects.filter(user=request.user).all()
    data.delete()
    return JsonResponse({"status": "success"}, status=200)
@csrf_exempt
def delete_book(request,id):
    data = Cart.objects.get(pk=id)
    data.delete()
    return HttpResponseRedirect(reverse('buy:cart'))
def show_json_by_id(request, id):
    data = Cart.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
def show_json_flutter(request, userId):
    data = Cart.objects.filter(user=userId)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")