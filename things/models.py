from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True)  # Adjust the max_length as needed
    description = models.CharField(max_length=120, blank=True)  # Use TextField for a slightly longer string
    quantity = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])