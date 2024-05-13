from django.urls import path
from .views import (PostCreateAPIView,
                    PostDeleteAPIView,
                    LikeCreateAPIView,
                    LikeDeleteAPIView,
                    CommentCreateAPIView)

urlpatterns = [
    path('api/posts/create/', PostCreateAPIView.as_view(), name='post-create'),
    path('api/posts/<int:pk>/delete/', PostDeleteAPIView.as_view(), name='post-delete'),
    path('api/likes/create/', LikeCreateAPIView.as_view(), name='like-create'),
    path('api/likes/delete/', LikeDeleteAPIView.as_view(), name='like-delete'),
    path('api/comment/create/', CommentCreateAPIView.as_view(), name='comment-create')
]
