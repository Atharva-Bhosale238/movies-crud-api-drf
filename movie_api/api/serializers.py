from rest_framework import serializers
from .models import Movie

#Movie object serializer to convert database objects(row) to python primitives
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id','title','director','releaseYear','genre','rating')