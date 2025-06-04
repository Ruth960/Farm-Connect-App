from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import register_user, login_user

urlpatterns = [
    path('register/', register_user),
    path('login/', login_user),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
