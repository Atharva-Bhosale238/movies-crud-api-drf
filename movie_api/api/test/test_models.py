from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import Movie
import datetime

class MovieModelTest(TestCase):
    #tests for Movie model field validations and constraints
    def test_create_valid_movie(self):
        #test that a valid movie can be created
        movie = Movie(
            title="Inception",
            director="Christopher Nolan",
            releaseYear=2010,
            genre="Sci-Fi",
            rating=9
        )
        movie.full_clean()  
        movie.save()
        self.assertEqual(Movie.objects.count(), 1)

    def test_blank_director_allowed(self):
        #director can be blank or null
        movie = Movie(
            title="No Director Movie",
            releaseYear=2020,
            genre="Drama",
            rating=7
        )
        movie.full_clean() 
        movie.save()
        self.assertEqual(Movie.objects.get(title="No Director Movie").director, None)

    def test_rating_validation(self):
        #rating must be between 1 and 10
        movie = Movie(
            title="Bad Rating",
            releaseYear=2015,
            genre="Comedy",
            rating=15  # invalid
        )
        with self.assertRaises(ValidationError):
            movie.full_clean()

    def test_release_year_validation(self):
        #release year must be between 1900 and current year
        next_year = datetime.datetime.now().year + 1
        movie = Movie(
            title="Future Movie",
            releaseYear=next_year, 
            genre="Sci-Fi",
            rating=5
        )
        with self.assertRaises(ValidationError):
            movie.full_clean()

    def test_unique_title_release_year_constraint(self):
        #test that unique constraint on title+releaseYear works
        Movie.objects.create(
            title="Inception",
            releaseYear=2010,
            genre="Sci-Fi"
        )
        duplicate_movie = Movie(
            title="Inception",
            releaseYear=2010,
            genre="Action"
        )
        with self.assertRaises(ValidationError):
            duplicate_movie.full_clean() 
