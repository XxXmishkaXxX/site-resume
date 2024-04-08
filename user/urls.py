from django.urls import path, include
from .views import CustomSignupView, CustomLoginView, CustomLogoutView


urlpatterns = [
    path('signup/', CustomSignupView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('', include('allauth.urls')),
]
