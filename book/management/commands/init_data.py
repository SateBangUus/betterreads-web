from django.shortcuts import render
import requests
from book.models import Book
from django.core.management.base import BaseCommand, CommandError

GOOGLE_BOOKS_API_URL = "https://www.googleapis.com/books/v1/volumes"
GOOGLE_BOOKS_API_KEY = "AIzaSyAs_56YG32-6Q9dQwiqa24fk64pm1CyeQ8"

class Command(BaseCommand):
    def fetch_books(self, category):
        queries = {
            'q': f'subject:{category}',
            'maxResults': 25,
            'key': GOOGLE_BOOKS_API_KEY,
            'langRestrict': 'en',
            'printType': 'books'
        }

        res = requests.get(GOOGLE_BOOKS_API_URL, params=queries)

        if res.status_code == 200:
            return res.json()['items']
        else:
            return []
    
    def insert_to_db(self, category, books):
        for book in books:
            book_data = book['volumeInfo']
            try:
                Book.objects.get(title=book_data.get('title', ''))
            except Book.DoesNotExist:
                Book.objects.create(
                    title=book_data.get('title', ''),
                    author=','.join(book_data.get('authors', [])),
                    publisher=book_data.get('publisher', ''),
                    published_date=book_data.get('publishedDate', ''),
                    description=book_data.get('description', ''),
                    genre=category,
                    image_link=f"https://books.google.com/books/publisher/content/images/frontcover/{book.get('id', '')}?fife=w600"
                )

    def handle(self, *args, **kwargs):
        Book.objects.all().delete()
        for category in ['Fiction', 'Science', 'Drama', 'Art', 'Biography', 'History']:
            books_data = self.fetch_books(category)
            self.insert_to_db(category, books_data)
            self.stdout.write(self.style.SUCCESS(f'Insertes books with {category} category.'))