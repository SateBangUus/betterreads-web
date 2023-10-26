# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bookID = models.CharField()
    amount = models.IntegerField()