from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Movie

def genre_default():
    return {'12': 0, '14': 0, '16': 0, '18': 0, '27': 0, '28': 0, '35': 0, '36': 0, '37': 0, '53':0, '80': 0, '99':0, '878':0, '9648':0, '10402':0, '10749':0, '10751':0, '10752':0, '10770':0 }


def genre_recommend_default():
    return {'12': 0, '14': 0, '16': 0, '18': 0, '27': 0, '28': 0, '35': 0, '36': 0, '37': 0, '53':0, '80': 0, '99':0, '878':0, '9648':0, '10402':0, '10749':0, '10751':0, '10752':0, '10770':0 }


# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    like_movies = models.ManyToManyField(Movie, related_name='like_users')
    genre_dict = models.JSONField(default=genre_default)
    genre_recommend_dict = models.JSONField(default=genre_recommend_default)