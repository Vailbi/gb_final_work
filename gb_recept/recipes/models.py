from django.db import models
from pytils.translit import slugify

# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Recipes.Status.PUBLISHED)


class Recipes(models.Model):
    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(max_length=255, verbose_name='Название рецепта')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Slug')
    content = models.TextField(blank=True, verbose_name='Описание рецепта')
    steps = models.CharField(max_length=255, verbose_name='Шаги приготовления')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.IntegerField(choices=Status.choices, default=Status.DRAFT, verbose_name='Статус')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='recipe',
                            verbose_name='Категории')
    tags = models.ManyToManyField('Tags', blank=True, related_name='tags', verbose_name='Тэги')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default=None, null=True, blank=True,
                              verbose_name='Фото')

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args,**kwargs)


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.CharField(max_length=100, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args,**kwargs)


class Tags(models.Model):
    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    name = models.CharField(max_length=100, db_index=True, verbose_name='Тэги')
    slug = models.CharField(max_length=100, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args,**kwargs)
