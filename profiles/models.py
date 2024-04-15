# import os
#
# from django.db import models
#
# from site_resume import settings
# from user.models import CustomUser
#
#
# def user_file_path(instance, filename, folder):
#     return os.path.join(folder, instance.user.email, filename)
#
#
# class Certificate(models.Model):
#     user = models.ForeignKey(CustomUser, related_name='certificates', on_delete=models.CASCADE)
#     image = models.ImageField(upload_to=lambda instance, filename: user_file_path(instance, filename,
#                                                                                   'certificates'),
#                               blank=True)
#
#
# class Award(models.Model):
#     user = models.ForeignKey(CustomUser, related_name='awards', on_delete=models.CASCADE)
#     image = models.ImageField(upload_to=lambda instance, filename: user_file_path(instance, filename, 'awards'),
#                               blank=True)
#
#
# class UserPhotos(models.Model):
#     user = models.ForeignKey(CustomUser, related_name='photos', on_delete=models.CASCADE)
#     image = models.ImageField(upload_to=lambda instance, filename: user_file_path(instance, filename, 'photos'),
#                               blank=True)
#
#
# class UserProfile(models.Model):
#
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
#     bio = models.TextField(max_length=1000, blank=True)
#     location = models.CharField(max_length=100, blank=True)
#     birth_date = models.DateField(null=True, blank=True)
#     links = models.TextField(max_length=1000, blank=True)
#     profile_picture = models.ImageField(upload_to=lambda instance, filename: user_file_path(instance, filename,
#                                                                                             'profile_pics'),
#                                         blank=True)
#
#     def __str__(self):
#         return f'Профиль {self.user}'
#
#     def save(self, *args, **kwargs):
#         if not self.profile_picture and self.user:
#             default_image = 'default_male.jpg' if self.user.sex == 'M' else 'default_female.jpg'
#             default_image_path = os.path.join(settings.MEDIA_ROOT, 'default_images', default_image)
#             if os.path.exists(default_image_path):
#                 self.profile_picture = os.path.join('default_images', default_image)
#         super().save(*args, **kwargs)
