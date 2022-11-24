from rest_framework import serializers
from .models import Movie, Genre, Comment, Rank
from django.contrib.auth import get_user_model


User = get_user_model()

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('id', 'name',)

class MovieListSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
        # fields = ('id', 'poster_path',)
        # fields = ('id', 'title', 'content', 'user', 'username')


class GenreListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'


class CommentListSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)
    
    movie = MovieSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('movie',)


class MovieSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('user', )


class RankSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)

    class Meta:
        model = Rank
        fields = ('id', 'user', 'movie', 'rank')
        read_only_fields = ('user', 'movie')