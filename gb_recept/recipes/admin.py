from django.contrib import admin
from .models import Recipes, Tags, Category
# Register your models here.


admin.site.register(Tags)
admin.site.register(Category)

@admin.register(Recipes)
class RecipesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    # readonly_fields = ['slug']
