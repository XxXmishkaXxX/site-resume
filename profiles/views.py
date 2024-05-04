import json

from allauth.account.forms import ChangePasswordForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import ModelFormMixin

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
    form_class = UserProfileForm  # Specify the form class directly
    template_name = 'edit_profile.html'

    def get_success_url(self):
        return self.request.path

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['change_password_form'] = ChangePasswordForm(user=self.request.user)
        return context

    def post(self, request, *args, **kwargs):

        form_name = request.POST.get('form_name')
        if form_name == 'changePasswordForm':

            change_password_form = ChangePasswordForm(user=request.user, data=request.POST)
            if change_password_form.is_valid():
                change_password_form.save()
                response_data = {
                    'message': 'Пароль успешно изменен'
                }

                return JsonResponse(response_data, status=200)
            else:
                return JsonResponse(change_password_form.errors, status=400)

        # Если форма смены пароля не отправлена, обрабатываем форму редактирования профиля
        return super().post(request, *args, **kwargs)

    def get_object(self, queryset=None):

        profile = super().get_object(queryset)

        if profile.user != self.request.user:
            return redirect(reverse('edit_profile', kwargs={'pk': self.request.user.pk}))

        return profile

    def form_valid(self, form):
        form.instance.user = self.request.user
        self.object = form.save()
        response_data = {
            'message': 'Внесенные изменения были сохранены'
        }
        return JsonResponse(response_data, status=200)

    def form_invalid(self, form):
        super().form_invalid(form)
        return JsonResponse(form.errors, status=400)
