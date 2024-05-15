from django.urls import path
from .views import (PostCreateAPIView,
                    PostDeleteAPIView,
                    LikeAPIView,
                    CommentCreateAPIView)

urlpatterns = [
    path('api/posts/create/', PostCreateAPIView.as_view(), name='post-create'),
    path('api/posts/<int:pk>/delete/', PostDeleteAPIView.as_view(), name='post-delete'),
    path('api/like/', LikeAPIView.as_view(), name='like'),
    path('api/comment/create/', CommentCreateAPIView.as_view(), name='comment-create')
]
