from django.urls import path, include
from .views import CustomSignupView, CustomLoginView, CustomLogoutView, check_email_confirmation


urlpatterns = [
    path('signup/', CustomSignupView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('check-email-confirmation/', check_email_confirmation, name='check_email_confirmation'),
    path('', include('allauth.urls')),

]
