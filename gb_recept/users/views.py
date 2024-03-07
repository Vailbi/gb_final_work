from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.shortcuts import render

from users.forms import LoginUserForm


# Create your views here.


class LoginUser(LoginView):

    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}
    success_url = 'home'

