from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from .models import Book, Review
import requests
from django.shortcuts import render
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book/book_list.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'book/book_detail.html', {'book': book})

def add_review(request, book_id):
    if request.method == 'POST':
        book = get_object_or_404(Book, pk=book_id)
        text = request.POST.get('text')
        Review.objects.create(user=request.user, book=book, text=text)
    return HttpResponseRedirect(reverse('book:book_detail', args=[book_id]))

def curator_section(request):
    # Add curator-related content here
    return render(request, 'book/curator_section.html')


GOOGLE_BOOKS_API_URL = "https://www.googleapis.com/books/v1/volumes"

def fetch_books_from_google_books_api(request):
    # Replace 'YOUR_API_KEY' with your actual API key if you have one
    api_key = 'YOUR_API_KEY'

    # Make a request to the Google Books API to fetch book data
    response = requests.get(f"{GOOGLE_BOOKS_API_URL}?q=YOUR_SEARCH_QUERY&key={api_key}")

    if response.status_code == 200:
        data = response.json()
        items = data.get('items', [])

        for item in items:
            volume_info = item.get('volumeInfo', {})
            title = volume_info.get('title', '')
            author = ", ".join(volume_info.get('authors', []))
            description = volume_info.get('description', '')

            # Create a new book in your database based on Google Books data
            book = Book(title=title, author=author, description=description)
            book.save()

        return render(request, 'book/success.html')
    else:
        return render(request, 'book/error.html')
