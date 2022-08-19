
from django.contrib import admin
from django.urls import re_path, include

from django.conf import settings
from django.conf.urls.static import static
from app import views


urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^index$',views.index, name='index'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
