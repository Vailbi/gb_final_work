
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from gb_recept import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
