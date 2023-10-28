from django.shortcuts import render, get_object_or_404
from .models import Book, Review
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

# View to display a list of all books
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

# View to display book details and reviews
def book_detail(request, book_id):
    book = Book.objects.get(pk=book_id)    
    reviews = Review.objects.filter(book=book)
    return render(request, 'book_detail.html', {'book': book, 'reviews': reviews})

# View to add a new review for a book
@login_required
def add_review(request, book_id):
    if request.method == 'POST' and request.is_ajax():
        book = Book.objects.get(pk=book_id)
        description = request.POST.get('description', '')
        rating = float(request.POST.get('rating', 0))

        if 1.0 <= rating <= 5.0:
            review = Review.objects.create(book=book, user=request.user, description=description, rating=rating)
            return JsonResponse({'status': 'success', 'message': 'Review added successfully'})

    return JsonResponse({'status': 'error', 'message': 'Invalid data'})

def get_reviews(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    reviews = Review.objects.filter(book=book)
    
    data = [
        {
            'rating': review.rating,
            'description': review.description,
        }
        for review in reviews
    ]
    
    return JsonResponse(data, safe=False)
