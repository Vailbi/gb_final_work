from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView

from recipes.models import Recipes, Category, Tags


def index(request):
    data = Recipes.objects.all()
    category = Category.objects.all()
    tags = Tags.objects.all()

    return render(request, 'recipes/index.html', {'data':data,
                                                  'cat': category,
                                                  'tags': tags})
