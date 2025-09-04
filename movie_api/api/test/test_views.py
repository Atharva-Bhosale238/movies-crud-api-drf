from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from ..models import Movie

class MovieAPITest(APITestCase):  
    def setUp(self):
        #Create a sample movie for testing
        self.movie = Movie.objects.create(
            title="Inception",
            director="Christopher Nolan",
            releaseYear=2010,
            genre="Sci-Fi",
            rating=9
        )
        self.list_url = reverse('movie-list')
        self.detail_url = reverse('movie-detail', kwargs={'id': self.movie.id})

    def test_get_movie_list(self):
        #Test retrieving all movies
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Inception")

    def test_get_movie_detail(self):
        #Test retrieving a single movie by ID
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['movie']['title'], "Inception")

    def test_create_movie_full(self):
        # Test creating a new movie with all details using POST request
        data = {
            "title": "Interstellar",
            "director": "Christopher Nolan",
            "releaseYear": 2014,
            "genre": "Sci-Fi",
            "rating": 10
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movie.objects.count(), 2)
        self.assertEqual(Movie.objects.get(title="Interstellar").rating, 10)

    def test_create_movie_partial(self):
        # Test creating a new movie with partial details using POST request
        data = {
            "title": "The martian",
            "releaseYear": 2016,
            "genre": "Space",
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movie.objects.count(), 2)
        self.assertEqual(Movie.objects.get(title="The martian").rating, None)

    def test_unique_movie_constraint(self):
        #Test duplicate title+releaseYear is rejected
        data = {
            "title": "Inception",
            "releaseYear": 2010,
            "genre": "Sci-Fi"
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Movie.objects.filter(title="Inception", releaseYear=2010).count(), 1)

    def test_update_movie_full(self):
        #Test full update with PUT request
        data = {
            "title": "Inception Updated",
            "director": "C. Nolan",
            "releaseYear": 2010,
            "genre": "Sci-Fi",
            "rating": 10
        }
        response = self.client.put(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.movie.refresh_from_db()
        self.assertEqual(self.movie.title, "Inception Updated")
        self.assertEqual(self.movie.rating, 10)

    def test_update_movie_partial(self):
        #Test partial update with PUT request
        data = {
            "title": "Inception Updated partially",
            "director": "Nolan",
            "genre": "Sci-Fi",
            "rating": 10
        }
        response = self.client.put(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.movie.refresh_from_db()
        self.assertEqual(self.movie.title, "Inception Updated partially")
        self.assertEqual(self.movie.rating, 10)
        self.assertEqual(self.movie.releaseYear,None)

    def test_delete_movie(self):
        #Test deleting a movie by id param
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Movie.objects.count(), 0)
