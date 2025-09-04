from django.http import JsonResponse
from django.shortcuts import HttpResponse, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Movie
from .serializers import MovieSerializer

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello world</h1>")


#Movie Api to handle all requests made to the api
class MovieApi(APIView):
    serializer_class = MovieSerializer

    #handles the post request
    def post(self, request, format=None):
        serializer  = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success":"movie saved successfully"}, status=status.HTTP_201_CREATED)
        return Response({"error":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    #handles the get request
    def get(self, request,id=None, format=None):
        if(id!=None):
            movie = get_object_or_404(Movie, id=id)
            serializer=self.serializer_class(movie)
            return Response({"movie":serializer.data},status=status.HTTP_200_OK)
        movie_items = Movie.objects.all()
        movies = self.serializer_class(movie_items, many=True)
        return Response(movies.data, status=status.HTTP_200_OK)
    
    #handles the put request
    def put(self, request,id=None, format=None):
        movie= get_object_or_404(Movie, id=id)
        serializer = self.serializer_class(movie, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response({"success":f"movie details updated with id {serializer['id'].value}"}, status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    #handles the delete request
    def delete(self, request, id=None, format=None):
        movie=get_object_or_404(Movie, id=id)
        movie.delete()
        return Response({"success":f"movie with id {id} deleted"}, status=status.HTTP_200_OK)