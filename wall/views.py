from rest_framework import permissions, status
from rest_framework.response import Response

from profiles.models import UserProfile
from profiles.serializers import UserProfileSerializer
from .models import Post, CommentPostModel, LikePostModel
from .serializers import CommentSerializer, LikeSerializer, PostSerializer
from .forms import PostCreateForm

from rest_framework.views import APIView


class PostCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        form = PostCreateForm(request.data)
        if form.is_valid():
            content = form.cleaned_data.get('content')
            images = request.FILES.getlist('images', [])
            videos = request.FILES.getlist('videos', [])
            author = request.user.userprofile

            post = Post.objects.create(content=content, author=author)

            for image in images:
                post.images.create(image=image)

            for video in videos:
                post.videos.create(video_file=video)

            return Response({'status': 'ok'}, status=status.HTTP_201_CREATED)

        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDeleteAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        post_id = kwargs.get('pk')
        try:
            post = Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            return Response({'detail': 'Пост не найден'}, status=status.HTTP_404_NOT_FOUND)

        if post.author != request.user.userprofile:
            return Response({'detail': 'У вас нет прав для удаления этого поста'}, status=status.HTTP_403_FORBIDDEN)

        post.delete()
        return Response({'detail': 'Пост успешно удален'}, status=status.HTTP_200_OK)


class LikeCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        post_id = request.data.get('post_id')
        user = request.user

        try:
            LikePostModel.objects.get(post_id=post_id, user=user)

            return Response({'detail': 'Лайк уже существует'}, status=status.HTTP_400_BAD_REQUEST)
        except LikePostModel.DoesNotExist:
            LikePostModel.objects.create(post_id=post_id, user=user)
            return Response({'detail': 'Лайк успешно создан'}, status=status.HTTP_201_CREATED)


class LikeDeleteAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):

        post_id = request.data.get('post_id')
        user = request.user

        try:
            like = LikePostModel.objects.get(post_id=post_id, user=user)
            like.delete()
            return Response({'detail': 'Лайк успешно удален'}, status=status.HTTP_200_OK)
        except LikePostModel.DoesNotExist:
            return Response({'detail': 'Лайк не найден'}, status=status.HTTP_404_NOT_FOUND)


class CommentCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            post_id = request.data.get('post_id')
            text = request.data.get('text')

            # Получаем объект поста
            post = Post.objects.get(pk=post_id)

            # Создаем комментарий для этого поста
            comment_data = {'post': post_id, 'text': text, "user_profile": request.user.userprofile}
            comment_serializer = CommentSerializer(data=comment_data)
            if comment_serializer.is_valid():
                comment_serializer.save()
                user_profile = UserProfileSerializer(request.user.userprofile, many=False)
                return Response({'comment': comment_serializer.data, 'user_profile':user_profile.data}, status=status.HTTP_201_CREATED)
            else:
                print(comment_serializer.errors)
                return Response(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Post.DoesNotExist:
            return Response({'detail': 'Пост с указанным ID не существует'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'detail': 'Произошла ошибка при добавлении комментария'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
