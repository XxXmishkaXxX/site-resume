from .views import (CustomSignupView, CustomLoginView, CustomLogoutView, check_email_confirmation, verified_email_view,
                    CustomConfirmEmailView, CustomResetPasswordView, CustomPasswordResetFromKeyView)
from django.urls import path, include, re_path

urlpatterns = [
    path('signup/', CustomSignupView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('check-email-confirmation/', check_email_confirmation, name='check_email_confirmation'),
    re_path(r"^confirm-email/(?P<key>[-:\w]+)/$", CustomConfirmEmailView.as_view(), name="account_confirm_email"),
    path('verified_email/', verified_email_view, name='verified_email'),
    path('password/reset/', CustomResetPasswordView.as_view(), name="reset-password"),
    re_path(r"^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$", CustomPasswordResetFromKeyView.as_view(),
            name="account_reset_password_from_key"),
    path('', include('allauth.urls')),

]
