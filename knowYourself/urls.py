from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import add_image_know_you
from .views import know_you_identity
from .views import know_you_learn
from .views import test
from home import views

urlpatterns = [
    path('test', test, name='test'),
    path('add_image_know_you', add_image_know_you, name='image_upload'),
    path('know_you_identity', know_you_identity, name='know_you_identity'),
    path('know_you_learn', know_you_learn, name='know_you_learn'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)