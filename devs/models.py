from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.

class Dev(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    # years = models.IntegerField(blank=True)
    years = models.PositiveIntegerField(default=10, validators=[MinValueValidator(18), MaxValueValidator(100)])
    country = models.CharField(blank=True, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)