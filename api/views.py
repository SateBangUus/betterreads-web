import requests
from django.shortcuts import render
from django.http import JsonResponse

GOOGLE_BOOKS_API_URL = "https://www.googleapis.com/books/v1/"
GOOGLE_BOOKS_API_KEY = "AIzaSyAs_56YG32-6Q9dQwiqa24fk64pm1CyeQ8"

# Create your views here.
def get_book(request):
    id = request.GET.get('id')
    res = requests.get(f"{GOOGLE_BOOKS_API_URL}volumes/{id}?key={GOOGLE_BOOKS_API_KEY}")
    return JsonResponse(res.json())

def get_books_by_title(request):
    title = request.GET.get('title')
    res = requests.get(f"{GOOGLE_BOOKS_API_URL}volumes?q=intitle:{title}&key={GOOGLE_BOOKS_API_KEY}")
    return JsonResponse(res.json())

def get_book_by_isbn(request):
    isbn_no = request.GET.get('isbn')
    res = requests.get(f"{GOOGLE_BOOKS_API_URL}volumes?q=isbn:{isbn_no}&key={GOOGLE_BOOKS_API_KEY}")
    return JsonResponse(res.json())

def get_books_by_author(request):
    author = request.GET.get('author')
    res = requests.get(f"{GOOGLE_BOOKS_API_URL}volumes?q=inauthor:{author}&key={GOOGLE_BOOKS_API_KEY}")
    return JsonResponse(res.json())

def get_books_by_genre(request):
    genre = request.GET.get('genre')
    res = requests.get(f"{GOOGLE_BOOKS_API_URL}volumes?q=subject:{genre}&key={GOOGLE_BOOKS_API_KEY}")
    return JsonResponse(res.json())

def get_id_by_isbn(request):
    isbn_no = request.GET.get('isbn')
    res = requests.get(f"{GOOGLE_BOOKS_API_URL}volumes?q=isbn:{isbn_no}&key={GOOGLE_BOOKS_API_KEY}")
    return JsonResponse({"id": res.json()["items"][0]["id"]})