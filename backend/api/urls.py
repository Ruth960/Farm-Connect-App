from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import register_user, login_user, ProductListingViewSet, ProductPhotoViewSet

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'products', ProductListingViewSet)
router.register(r'product-photos', ProductPhotoViewSet)

urlpatterns = [
    path('register/', register_user),
    path('login/', login_user),
    path('', include(router.urls)),  # Include router URLs
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
