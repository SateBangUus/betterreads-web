from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.CharField(max_length=100)
    rating = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])

class Curator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    is_curator = models.BooleanField(default=False)