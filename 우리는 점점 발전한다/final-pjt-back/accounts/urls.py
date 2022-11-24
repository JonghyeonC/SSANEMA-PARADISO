from django.urls import path
from . import views

# app_name = 'accounts'

urlpatterns = [
    path('mypage/', views.mypage),
    path('profile/<username>/', views.profile),
    path('follow/<username>/', views.follow),
    path('like_movies/<int:movie_pk>/', views.like_movies),
    path('tinder_like_movies/<int:movie_pk>/', views.tinder_like_movies),
    path('tinder_dislike_movies/<int:movie_pk>/', views.tinder_dislike_movies),
    path('recommend/', views.recommend),
]