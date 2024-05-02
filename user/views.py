import json

from django.shortcuts import render, redirect, reverse
from allauth.account.views import SignupView, LoginView, ConfirmEmailView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.views.generic import RedirectView
from .forms import CustomSignupForm
from allauth.account.models import EmailAddress
from django.http import JsonResponse


def check_email_confirmation(request):
    if request.user.is_authenticated:

        user = request.user
        email_confirmed = EmailAddress.objects.filter(user=user, verified=True).exists()

        return JsonResponse({'confirmed': email_confirmed})
    else:
        return JsonResponse({'error': 'User is not authenticated'})


class CustomSignupView(SignupView):
    form_class = CustomSignupForm
    template_name = 'signup.html'

    def form_invalid(self, form):
        super().form_invalid(form)
        data = form.errors.as_json()
        return JsonResponse(json.loads(data), status=400, safe=False)


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
        super().form_invalid(form)
        data = form.errors.as_json()
        return JsonResponse(json.loads(data), status=400, safe=False)


class CustomLogoutView(RedirectView):
    url = reverse_lazy('main-page')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)


class CustomConfirmEmailView(ConfirmEmailView):
    def get_redirect_url(self):
        return reverse('verified_email')


def verified_email_view(request):
    return render(request, 'verified_email.html')
