from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('simple_import/', include('simple_import.urls', namespace='simple_import')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
