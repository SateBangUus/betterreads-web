from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.db.models import Sum, Avg
from django.core import serializers
from book.models import Book
from book.models import Review
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def show_main(request):
    if request.user.is_authenticated:
        books = Book.objects.all().order_by('title')
        context = {
            'books' : books,
        }
        return render(request, 'main.html', context)
    return HttpResponseRedirect('/auth/login/')

def search_books(request):
    search_term = request.GET.get('search_term', '')
    filtered_books = Book.objects.filter(title__icontains=search_term)
    book_data = [{'title': book.title, 'author': book.author, 'publisher': book.publisher, 'description': book.description, 'genre': book.genre, 'image_link': book.image_link, 'id': book.id} for book in filtered_books]
    return JsonResponse({'books': book_data})

def search_books_blank(request):
    search_term = request.GET.get('search_term', '')
    filtered_books = Book.objects.filter(title__icontains=search_term).order_by('title')
    book_data = [{'title': book.title, 'author': book.author, 'publisher': book.publisher, 'description': book.description, 'genre': book.genre, 'image_link': book.image_link, 'id': book.id} for book in filtered_books]
    return JsonResponse({'books': book_data})

@csrf_exempt
def search_books_flutter(request):
    search_term = request.GET.get('search_term', '')
    filtered_books = Book.objects.filter(title__icontains=search_term)
    book_data = [{
        "model": "book.book",
        "pk": book.pk,
        "fields": {
            'title': book.title, 
            'author': book.author, 
            'publisher': book.publisher, 
            'published_date': book.published_date,
            'description': book.description, 
            'genre': book.genre, 
            'image_link': book.image_link, 
        }
    } for book in filtered_books]
    return JsonResponse(book_data, safe=False)

def show_books_flutter(request):
    allbooks = Book.objects.all()
    book_data = [{
        "model": "book.book",
        "pk": book.pk,
        "fields": {
            'title': book.title, 
            'author': book.author, 
            'publisher': book.publisher, 
            'published_date': book.published_date,
            'description': book.description, 
            'genre': book.genre, 
            'image_link': book.image_link, 
        }
    } for book in allbooks]
    return JsonResponse(book_data, safe=False)