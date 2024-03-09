from django import template
from recipes.models import Category, Tags


register = template.Library()


menu = [{'title': "Главная страница", 'url_name': 'home'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        ]


@register.inclusion_tag('recipes/list_tags.html')
def show_all_tags():
    return {'tags': Tags.objects.all()}


@register.simple_tag
def get_menu():
    return menu

@register.inclusion_tag('recipes/cat_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected}