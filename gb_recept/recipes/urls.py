from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('recipe/<slug:slug>/', views.ShowPost.as_view(), name='recipe'),
    path('category/<slug:slug>/', views.ShowCat.as_view())
]

