from django.urls import path

from .views import ProfileCreateView, ProfileView, ProfileEditView

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create_profile'),
    path('<int:pk>/', ProfileView.as_view(), name='profile_user'),
    path('edit/<int:pk>/', ProfileEditView.as_view(), name='edit_profile')

]