from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Movie, Collection

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'],password=validated_data['password'])
        return user


class MovieSerializer(serializers.Serializer):
    
    title = serializers.CharField()
    description = serializers.CharField()
    genres = serializers.CharField()
    uuid = serializers.CharField()


# Collection Section --------------------------->

class MoviecollectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id','title', 'description', 'genres', 'uuid')

class CollectionSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True)  # Nested serializer for Movie model

    class Meta:
        model = Collection
        fields = ('id','title', 'description', 'movies')

class MovieSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id','title', 'description', 'genres', 'uuid')

class CollectionSerializer1(serializers.ModelSerializer):
    movies = MovieSerializer(many=True)

    class Meta:
        model = Collection
        fields = ('uuid', 'title', 'description', 'movies')
        def update(self, instance, validated_data):
            movies_data = validated_data.pop('movies', [])
            instance = super().update(instance, validated_data)
            for movie_data in movies_data:
                movie, _ = Movie.objects.get_or_create(**movie_data)
                instance.movies.add(movie)
            return instance