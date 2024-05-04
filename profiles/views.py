import json

from allauth.account.forms import ChangePasswordForm
from django.contrib.auth.decorators import login_required
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from .models import UserProfile
from .forms import UserProfileForm


class ProfileCreateView(CreateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'create_profile.html'

    def form_valid(self, form):
        print(form.cleaned_data)
        form.instance.user = self.request.user
        print(form.data)
        return super().form_valid(form)

    def form_invalid(self, form):
        super().form_invalid(form)
        data = form.errors.as_json()
        return JsonResponse(json.loads(data), status=400, safe=False)

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated and hasattr(self.request.user, 'userprofile'):
            return redirect('profile_user', pk=self.request.user.userprofile.pk)
        return super().dispatch(request, *args, **kwargs)


class ProfileView(View):

    def get(self, reqeust, pk):
        user = self.request.user
        profile = UserProfile.objects.get(pk=pk)
        context = {
            'user': user,
            'avatar': profile.avatar,
            'full_name': profile.full_name,
            'bio': profile.bio,
            'country': profile.country.name,
            'city': profile.city.name,
            'birth_date': profile.birth_date,
            'profile_pk': profile.pk,
        }
        return render(reqeust, 'profile.html', context)


@method_decorator(login_required, name='dispatch')
class ProfileEditView(UpdateView):
    model = UserProfile
    template_name = 'edit_profile.html'
    form_class = UserProfileForm
    success_url = None

    def get_object(self, queryset=None):

        profile = super().get_object(queryset)

        if profile.user != self.request.user:

            return redirect(reverse('edit_profile', kwargs={'pk': self.request.user.pk}))

        return profile

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)