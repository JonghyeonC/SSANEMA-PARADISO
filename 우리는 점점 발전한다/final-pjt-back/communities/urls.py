# from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path
from . import views


urlpatterns = [
    path('community/', views.community_list),
    path('community/<int:community_pk>/', views.community_detail),
    path('community/<int:community_pk>/comments/', views.comment),
    path('community/comments/<int:comment_pk>/', views.comment_detail),
    # # 필수 작성
    # path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # # optional UI
    # path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
