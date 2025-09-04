from django.urls import path
from . import views
from .views import MovieApi

urlpatterns = [
    #both the urls /movies and /movies/<movie_id> are handled by the same view
    path('movies/', MovieApi.as_view(), name="movie-list"),
    path('movies/<str:id>/', MovieApi.as_view(), name="movie-detail"),
]
