from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Book(models.Model):
    title = models.TextField()
    author = models.TextField()
    publisher = models.TextField()
    published_date = models.CharField(max_length=10, null=True)
    description = models.TextField()
    genre = models.TextField()
    image_link = models.TextField()

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    rating = models.FloatField(validators=[MinValueValidator(1, 0), MaxValueValidator(5, 0)])
    is_curator = models.BooleanField(default=False)
