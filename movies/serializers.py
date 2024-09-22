from rest_framework import serializers
from movies.models import Movie
from genres.models import Genre
from actors.models import Actor
from actors.serializers import ActorSerializer
from genres.serializers import GenreSerializer
from django.db.models import Avg


class MovieModelSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        # reviews =  obj.reviews.all()
        # if reviews:
        #     sum_reviews = 0
        #     for review in reviews:
        #      sum_reviews += review.stars
        #     reviews_count = reviews.count()
        #     return round(sum_reviews / reviews_count, 1)
        if rate:
            return round(rate, 1)
        return None

    def validate_release_date(self, value):
        if value.year < 1990:
            raise serializers.ValidationError('A data de lançameto nao pode ser menor que 1990')
        return value

    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError('O resumo nao pode ter mais de 200 caracteres')
        return value


class MovieListDetailSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    genre = GenreSerializer()
    rate = serializers.SerializerMethodField(read_only=True)
   
    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']
   
    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        if rate:
            return round(rate, 1)

        return None