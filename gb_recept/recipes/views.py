from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView

from recipes.models import Recipes, Category, Tags


def index(request):
    data = Recipes.objects.all()
    category = Category.objects.all()
    tags = Tags.objects.all()

    return render(request, 'recipes/index.html', {'posts': data,
                                                  'cat': category,
                                                  'tags': tags})


class ShowPost(DetailView):
    model = Recipes
    template_name = 'recipes/post.html'
    context_object_name = 'posts'

    # slug_url_kwarg = 'post_slug'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return self.get_mixin_context(context, title=context['posts'])

    def get_object(self, queryset=None):
        return get_object_or_404(Recipes.published, slug=self.kwargs[self.slug_url_kwarg])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = self.get_object().title
        context['title'] = recipe
        return context


class ShowCat(ListView):
    model = Category
    template_name = 'recipes/index.html'
    context_object_name = 'posts'
    allow_empty = True

    def get_queryset(self):
        return Recipes.published.filter(cat__slug=self.kwargs['slug']).select_related('cat')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = Category.objects.get(slug=self.kwargs['slug']).name
        context['title'] = title
        return context


class ShowTag(ListView):
    model = Tags
    template_name = 'recipes/index.html'
    context_object_name = 'posts'
    allow_empty = True


    def get_queryset(self):
        return Recipes.published.filter(tags__slug=self.kwargs['slug']).select_related('cat')