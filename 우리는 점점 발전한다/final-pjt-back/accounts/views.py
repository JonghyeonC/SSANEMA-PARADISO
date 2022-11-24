from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProfileSerializer
from rest_framework import status

from movies.models import Movie, Genre

# Create your views here.
User = get_user_model()

@api_view(['GET'])
def mypage(request):
    username = request.user.username
    user = get_object_or_404(get_user_model(), username=username)
    serializer = ProfileSerializer(user)
    return Response(serializer.data)
    

@api_view(['GET'])
def profile(request, username):
    user = get_object_or_404(User, username=username)
    serializer = ProfileSerializer(user)
    return Response(serializer.data)


@api_view(['POST'])
def follow(request, username):
    guest = request.user
    user = get_object_or_404(get_user_model(), username=username)

    if guest != user:
        if user.followers.filter(pk=guest.pk).exists():
            user.followers.remove(guest)
        else:
            user.followers.add(guest)
    serializer = ProfileSerializer(user)
    return Response(serializer.data)

@api_view(['POST'])
def like_movies(request, movie_pk):
    username = request.user.username
    movie = get_object_or_404(Movie, pk=movie_pk)
    # Community.objects.all()
    genres = movie.genres.all()
    user = get_object_or_404(get_user_model(), username=username)
    if user.like_movies.filter(pk=movie_pk).exists():
        user.like_movies.remove(movie_pk)
        for genre in genres:
            user.genre_dict[str(genre.id)] -= 1
    else:
        user.like_movies.add(movie_pk)
        for genre in genres:
            user.genre_dict[str(genre.id)] += 1
    user.save()
    serializers = ProfileSerializer(user)
    return Response(serializers.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def tinder_like_movies(request, movie_pk):
    username = request.user.username
    movie = get_object_or_404(Movie, pk=movie_pk)
    genres = movie.genres.all()
    user = get_object_or_404(get_user_model(), username=username)
    if user.like_movies.filter(pk=movie_pk).exists():
        pass
    else:
        user.like_movies.add(movie_pk)
        for genre in genres:
            user.genre_dict[str(genre.id)] += 1
    user.save()
    serializers = ProfileSerializer(user)
    return Response(serializers.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def tinder_dislike_movies(request, movie_pk):
    username = request.user.username
    movie = get_object_or_404(Movie, pk=movie_pk)
    genres = movie.genres.all()
    user = get_object_or_404(get_user_model(), username=username)
    if user.like_movies.filter(pk=movie_pk).exists():
        user.like_movies.remove(movie_pk)
        for genre in genres:
            user.genre_dict[str(genre.id)] -= 1
    else:
        pass
    user.save()
    serializers = ProfileSerializer(user)
    return Response(serializers.data, status=status.HTTP_200_OK)


import random
import math
@api_view(['GET'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
def recommend(request):
    username = request.user.username
    person = get_object_or_404(get_user_model(), username=username)
    person_genre_dict = person.genre_dict
    

    # 장르 선호 순으로 배열 [1등, 2등, 3등] = [[장르, 점수], [장르, 점수], [장르, 점수]]
    person_genre = [[0, 0], [0, 0], [0, 0]]
    for key, val in person_genre_dict.items():
        for grade in range(3):
            if person_genre[grade][1] < val:
                person_genre[grade][0] = key
                person_genre[grade][1] = val
                break
            elif person_genre[grade][1] == val:
                if (grade == 0 or grade == 1) and person_genre[grade + 1][1] != 0:
                    person_genre[grade][0] = key
                    person_genre[grade][1] = val
                    break
                person_genre[grade][0] = key
                person_genre[grade][1] = val
               

    
    # 각 등수별 불러올 영화수
    total = person_genre[0][1] + person_genre[1][1] + person_genre[2][1]
    first_cnt = round((person_genre[0][1] / total) * 50)
    second_cnt = round((person_genre[1][1] / total) * 50)
    third_cnt = round((person_genre[2][1] / total) * 50)
    if first_cnt + second_cnt + third_cnt > 50:
        first_cnt -= abs(50 - (first_cnt + second_cnt + third_cnt))
    elif first_cnt + second_cnt + third_cnt < 50:
        first_cnt += abs(50 - (first_cnt + second_cnt + third_cnt))
    

    person.genre_recommend_dict = {}
    person.genre_recommend_dict[str(person_genre[0][0])] = first_cnt
    person.genre_recommend_dict[str(person_genre[1][0])] = second_cnt
    person.genre_recommend_dict[str(person_genre[2][0])] = third_cnt

    person.save()
    serializer = ProfileSerializer(person)
    return Response(serializer.data)


