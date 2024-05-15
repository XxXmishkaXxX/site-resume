import json
from allauth.account.forms import ChangePasswordForm
from django.views.generic import CreateView, UpdateView, DetailView, TemplateView
from wall.models import Post, LikePostModel
from django.contrib.auth.decorators import login_required

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

    def get_success_url(self):
        return reverse('profile_user', kwargs={'pk': self.object.pk})

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


class ProfileView(DetailView):
    model = UserProfile
    template_name = 'profile.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.get_object()
        posts = Post.objects.filter(author=profile).order_by('-created_at')
        context['posts'] = posts
        return context


@method_decorator(login_required, name='dispatch')
class ProfileEditView(UpdateView):
    model = UserProfile
    template_name = 'edit_profile.html'
    form_class = UserProfileForm
    success_url = None

    def get_success_url(self):
        return self.request.path

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['change_password_form'] = ChangePasswordForm(user=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        print(request.POST)
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
