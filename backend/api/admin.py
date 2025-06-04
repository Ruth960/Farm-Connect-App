from django.contrib import admin
from .product_models import ProductListing, ProductPhoto

class ProductPhotoInline(admin.TabularInline):
    model = ProductPhoto
    extra = 1

@admin.register(ProductListing)
class ProductListingAdmin(admin.ModelAdmin):
    inlines = [ProductPhotoInline]
    list_display = ('title', 'quantity', 'price', 'unit', 'location', 'availability_date', 'status')
    search_fields = ('title', 'description', 'location')

@admin.register(ProductPhoto)
class ProductPhotoAdmin(admin.ModelAdmin):
    list_display = ('product', 'image', 'uploaded_at')
