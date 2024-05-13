from django import forms
from .models import Post


class PostCreateForm(forms.ModelForm):
    MAX_FILES = 5

    images = forms.ImageField(
        widget=forms.FileInput(attrs={'allow_multiple_selected': True}),
        required=False,
        label='images')
    videos = forms.FileField(
        widget=forms.FileInput(attrs={'allow_multiple_selected': True}),
        required=False,
        label='videos')
    content = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4}),
        required=True, label='content')

    class Meta:
        model = Post
        fields = ('content', 'images', 'videos',)

    def clean_images(self):
        images = self.data.getlist('images')
        if images and len(images) > self.MAX_FILES:
            raise forms.ValidationError(f"Максимальное количество изображений для загрузки - {self.MAX_FILES}.")
        return images

    def clean_videos(self):
        videos = self.cleaned_data.get('videos')
        if videos and len(videos) > self.MAX_FILES:
            raise forms.ValidationError(f"Максимальное количество видео для загрузки - {self.MAX_FILES}.")
        return videos
