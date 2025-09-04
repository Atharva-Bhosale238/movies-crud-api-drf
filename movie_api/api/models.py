from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid
import datetime

# Create your models here.
class Movie(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=30, blank=False)
    director = models.CharField(max_length=20, blank=True, null=True)
    releaseYear = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(datetime.datetime.now().year)], blank=True, null=True)
    genre = models.CharField(max_length=20)
    rating = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)], blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title', 'releaseYear'], name='unique_movie')
        ]
