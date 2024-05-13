import os
from django.db import models
from profiles.models import UserProfile


class Post(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    content = models.TextField()
    likes_count = models.IntegerField(default=0)
    views_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.author.full_name} at {self.created_at}"


class ImagePost(models.Model):
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images')

    def image_upload_path(self, filename):
        return os.path.join('post_images', self.post.author.user.email, filename)

    def save(self, *args, **kwargs):
        self.image.name = self.image_upload_path(self.image.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Image for post: {self.post}"


class VideoPost(models.Model):
    post = models.OneToOneField(Post, related_name='video', on_delete=models.CASCADE)
    video_file = models.FileField(upload_to='post_videos', null=True, blank=True)
    video_url = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"Video for post: {self.post}"


class CommentPostModel(models.Model):
    user_profile = models.ForeignKey(UserProfile, related_name='comment', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comment_for_post', on_delete=models.CASCADE)
    text = models.TextField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment {self.user_profile.full_name} to post: {self.post}"


class LikePostModel(models.Model):
    user_profile = models.ForeignKey(UserProfile, related_name='like', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='like_for_post', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Like {self.user_profile.full_name} to post: {self.post}"
