from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from home import views

urlpatterns = [
    path('add_image_know_you', add_image_know_you, name='image_upload'),
    path('success', success, name = 'success'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)