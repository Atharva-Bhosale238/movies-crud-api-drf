from django.http import JsonResponse
from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Movie
from .serializers import MovieSerializer

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello world</h1>")

class MovieApi(APIView):
    serializer_class = MovieSerializer

    def post(self, request, format=None):
        title = request.POST.get('title')
        director = request.POST.get('director')
        releaseYear = request.POST.get('releaseYear')
        genre = request.POST.get('genre')
        rating = request.POST.get('rating')
        if (title=='' or director=='' or releaseYear=='' or genre=='' or rating==''):
            return Response({"error":"incomplete details"}, status=status.HTTP_400_BAD_REQUEST)
        movie = Movie(title=title, director=director, releaseYear=releaseYear, genre=genre, rating=rating)
        movie.save()
        return Response({"success":"movie saved successfully"}, status=status.HTTP_201_CREATED)

    def get(self, request, format=None):
        movie_items = Movie.objects.values()
        movies = list(movie_items)
        return Response({"movies" : movies}, status=status.HTTP_200_OK)
    

