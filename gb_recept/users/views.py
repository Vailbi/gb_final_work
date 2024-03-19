from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from recipes.models import Recipes
from users.forms import LoginUserForm, RegisterUserForm, ProfileUserForm, UserPasswordChange


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}
    success_url = reverse_lazy('home')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    extra_context = {'title': 'Регистрация'}
    success_url = reverse_lazy('home')


class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'users/profile.html'
    extra_context = {'title': "Профиль пользователя"}

    def get_success_url(self):
        return reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        """ Теперь профайл будет открываться только для текущего пользователя,
        либо сделано перенаправление на страницу авторизации для неавторизованных пользователей. """
        return self.request.user


class AddRecipe(LoginRequiredMixin, CreateView):
    model = Recipes
    fields = ['title', 'content', 'steps', 'cooking_time', 'is_published', 'cat', 'tags', 'photo']
    template_name = 'users/addrecipe.html'
    success_url = reverse_lazy('home')
    extra_context = {'title': 'Добавление рецепта'}


    def form_valid(self, form):
        '''Проверка и сохранения автора-юзера в модель Women'''
        w = form.save(commit=False)
        w.author = self.request.user
        return super().form_valid(form)


class ChangePassword(PasswordChangeView):
    form_class = UserPasswordChange
    success_url = reverse_lazy("users:password_change_done")
    template_name = "users/password_change_form.html"
    extra_context = {'title': 'Регистрация'}