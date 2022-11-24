# from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path
from . import views


urlpatterns = [
    path('', views.movie_list),
    path('genre/', views.genre_list),
    path('movies/<int:movie_pk>/', views.movie_detail),
    path('movies/<int:movie_pk>/comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('rank/<int:movie_pk>/created/', views.rank),
    path('rank/updated/<int:movie_pk>/', views.rank_update),
    path('movies/<int:movie_pk>/comments_create/', views.comment_create),
    path('genres/', views.genres),
    # # 필수 작성
    # path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # # optional UI
    # path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
