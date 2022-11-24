from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

class Genre(models.Model):
    name = models.CharField(max_length=50)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_genres')

    def __str__(self):
        return self.name


# Create your models here.
class Movie(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie_id = models.IntegerField()
    title = models.CharField(max_length=100)
    original_title = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre)
    overview = models.TextField()
    popularity = models.TextField()
    backdrop_path = models.TextField(null=True)
    poster_path = models.TextField()
    country = models.TextField(null=True)
    release_date = models.TextField()
    runtime = models.IntegerField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    cast_info = models.JSONField(null=True)
    crew_info = models.JSONField(null=True)
    video_url = models.JSONField(null=True)
    similar_movies = models.JSONField(null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Rank(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="ranks")
    rank = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)