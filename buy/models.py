# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from book.models import Book

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    amount = models.IntegerField()