from django.shortcuts import render, get_object_or_404
from .models import Book, Review
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt  # Import csrf_exempt
from django.http import HttpResponseRedirect
from django.urls import reverse
import json

# View to display a list of all books
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

# View to display book details and reviews
def book_detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    all_reviews = Review.objects.filter(book=book)
    
    curator_reviews = all_reviews.filter(user__profile__is_curator=True)

    non_curator_reviews = all_reviews.filter(user__profile__is_curator=False)

    
    context = {
        'book': book,
        'curator_reviews': curator_reviews,
        'non_curator_reviews': non_curator_reviews,
    }

    return render(request, 'book_detail.html', context)
# View to add a new review for a book
from django.http import JsonResponse

@login_required
@csrf_exempt
def add_review(request, book_id):
    if request.method == 'POST':
        # Get the logged-in user
        user = request.user
        book = Book.objects.get(pk=book_id)
        body = json.loads(request.body)
        # Check if the user has already reviewed the book
        existing_review = Review.objects.filter(book=book, user=user).first()

        if existing_review:
            # If the user has already reviewed the book, you can return an error response
            return JsonResponse({'status': 'error', 'message': 'You have already reviewed this book'})

        description = body.get('description', '')
        rating = float(body.get('rating', 0))

        if 1.0 <= rating <= 5.0:
            # Create a new review associated with the logged-in user
            Review.objects.create(book=book, user=user, description=description, rating=rating)
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

@login_required
@csrf_exempt
def delete_review(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        review_id = body.get('review_id')

        try:
            review = Review.objects.get(id=review_id)
            if review.user == request.user:
                review.delete()
                return JsonResponse({'status': 'success', 'message': 'Review deleted successfully'})
            else:
                return JsonResponse({'status': 'error', 'message': 'You are not authorized to delete this review'})
        except Review.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Review not found'})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid data'})