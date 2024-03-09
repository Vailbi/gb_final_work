from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from recipes.models import Recipes, Category


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин или Email', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput())
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Повтор пароля", widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        labels = {
            'email': 'E-mail',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }


class ProfileUserForm(forms.ModelForm):
    username = forms.CharField(disabled=True, label='Логин', widget=forms.TextInput())
    email = forms.CharField(disabled=True, label='E-mail', widget=forms.TextInput())

    # disabled=True этот параметр не дает редактировать поле
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }


# class AddRecipeForm(forms.ModelForm):
#     class Meta:
#         model = Recipes
#         fields = ['title', 'content', 'steps', 'cooking_time', 'is_published', 'cat', 'tags', 'photo']
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-input'}),
#             'content': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
#         }
#         labels = {
#             'slug': 'URL '
#         }
#
#     def clean_title(self):
#         title = self.cleaned_data['title']
#         if len(title) > 50:
#             raise ValidationError('Слишком большое название')
#         return title
#
#     slug = forms.CharField(required=True)
#     cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='Категория не выбрана')
#
