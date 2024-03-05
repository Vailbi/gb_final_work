from django.contrib import admin
from .models import Recipes, Tags, Category
# Register your models here.

@admin.register(Recipes)
class RecipesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}