from django.urls import path
from . import views
from .views import MovieApi

urlpatterns = [
    path('movies/', MovieApi.as_view(), name="movies"),
    path('movies/<str:id>/', MovieApi.as_view(), name="movies"),
]
