from rest_framework.response import Response
from rest_framework.decorators import api_view
# Authentication Decorators
from rest_framework.decorators import authentication_classes

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import MovieListSerializer, MovieSerializer, GenreListSerializer, CommentSerializer, GenreSerializer, RankSerializer
# , CommunitySerializer, CommunityCommentSerializer
from .models import Movie, Genre, Comment, Rank
from accounts.models import User

from django.contrib.auth import get_user_model


@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def movie_list(request):
    if request.method == 'GET':
        # articles = Article.objects.all()
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def genre_list(request):
    if request.method == 'GET':
        # articles = Article.objects.all()
        genres = get_list_or_404(Genre)
        serializer = GenreListSerializer(genres, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GenreListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def movie_detail(request, movie_pk):
    # article = Article.objects.get(pk=article_pk)
    movie = get_object_or_404(Movie, pk=movie_pk)

    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        print(serializer.data)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET'])
def comment_list(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        # comments = Comment.objects.all()
        comments = movie.comment_set.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, movie_pk):
    username = request.user.username
    user = get_object_or_404(User, username=username)
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=user, movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def comment_detail(request, comment_pk):
    username = request.user.username
    user = get_object_or_404(User, username=username)
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        if user == comment.user:
            comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
def rank(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    # username = request.user.username
    # user = get_object_or_404(User, username=username)
    if request.method == 'POST':
        username = request.user.username
        serializer = RankSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET','PUT'])
def rank_update(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    username = request.user.username
    user = get_object_or_404(User, username=username)
    rank = get_object_or_404(Rank, user=user, movie=movie)
    if request.method == 'GET':
        serializer = RankSerializer(rank)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RankSerializer(rank, data=request.data)
        if serializer.is_valid(raise_exception=True):
            
            serializer.save()
            return Response(serializer.data)


# @api_view(['GET', 'POST'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
def genres(request):
    person = get_object_or_404(get_user_model(), username=request.username)
    # 해당 유저가 어떤 장르를 가장 좋아하는지 체크하기 위한 Json(dict type)
    person_genre_dict = person.genre_dict

    if request.method == 'GET':
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        for data in request.data:
            # MtoM field 관리
            person.like_genres.add(data)
            # Json field 관리
            person_genre_dict[str(data)] += 1
        person.save()
        return Response(status=status.HTTP_201_CREATED)


# @api_view(['GET', 'POST'])
# # @permission_classes([IsAuthenticated])
# def community_list(request):
#     if request.method == 'GET':
#         # articles = Article.objects.all()
#         communities = get_list_or_404(Community)
#         serializer = CommunitySerializer(communities, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = CommunitySerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             # serializer.save(user=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'DELETE', 'PUT'])
# def community_detail(request, community_pk):
#     # article = Article.objects.get(pk=article_pk)
#     community = get_object_or_404(Community, pk=community_pk)

#     if request.method == 'GET':
#         serializer = CommunitySerializer(community)
#         print(serializer.data)
#         return Response(serializer.data)
    
#     elif request.method == 'DELETE':
#         community.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     elif request.method == 'PUT':
#         serializer = CommunitySerializer(community, data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)