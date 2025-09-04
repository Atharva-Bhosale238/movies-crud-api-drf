from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid
import datetime

# Create your models here.

#Movie model that stores data related to the movie in the database
class Movie(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=30, blank=False)
    director = models.CharField(max_length=20, blank=True, null=True)
    releaseYear = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(datetime.datetime.now().year)], blank=True, null=True)
    genre = models.CharField(max_length=20)
    rating = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)], blank=True, null=True)

    class Meta:
        #constraint to deny duplicate movie entries based on title and release year
        constraints = [
            models.UniqueConstraint(fields=['title', 'releaseYear'], name='unique_movie')
        ]
