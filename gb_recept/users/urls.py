from django.urls import path
from django.contrib.auth.views import LogoutView
from users import views

app_name = 'users'

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('profile/', views.ProfileUser.as_view(), name='profile'),
    path('addrecipe/', views.AddRecipe.as_view(), name='addrecipe'),
]