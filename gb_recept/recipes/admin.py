from django.contrib import admin
from .models import Recipes, Tags, Category
# Register your models here.

admin.site.register(Recipes)
admin.site.register(Tags)
admin.site.register(Category)
