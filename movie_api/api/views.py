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
        movie = Movie(title=title, director=director, releaseYear=releaseYear, genre=genre, rating=rating)

        return Response({}, status=status.HTTP_201_CREATED)
    

