from django.shortcuts import render, redirect
from allauth.account.views import SignupView, LoginView, EmailVerificationSentView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import logout
from django.views.generic import RedirectView
from django.urls import reverse
from .forms import CustomSignupForm


class CustomSignupView(SignupView):
    form_class = CustomSignupForm
    template_name = 'signup.html'

    def form_invalid(self, form):
        messages.error(self.request, 'error registration')
        return super().form_invalid(form)


class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('main-page')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('main-page')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return self.success_url

    def form_invalid(self, form):
        messages.error(self.request, 'Неудачный вход')
        return super().form_invalid(form)


class CustomLogoutView(RedirectView):
    url = reverse_lazy('main-page')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)





