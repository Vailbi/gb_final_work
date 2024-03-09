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

    return render(request, 'recipes/index.html', {'data': data,
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


class ShowCat(ListView):
    pass
