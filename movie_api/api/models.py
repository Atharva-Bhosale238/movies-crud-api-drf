from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator, MaxLengthValidator
import uuid

# Create your models here.
class Movie(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=30, blank=False)
    director = models.CharField(max_length=20)
    releaseYear = models.IntegerField(max_length=4, validators=[MinLengthValidator(4), MaxLengthValidator(4)])
    genre = models.CharField(max_length=20)
    rating = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])

