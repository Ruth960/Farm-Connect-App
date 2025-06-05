from rest_framework import serializers
from .product_models import ProductListing, ProductPhoto

class ProductPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPhoto
        fields = ['id', 'image', 'uploaded_at']

class ProductListingSerializer(serializers.ModelSerializer):
    photos = ProductPhotoSerializer(many=True, read_only=True)
    
    class Meta:
        model = ProductListing
        fields = [
            'id', 
            'title', 
            'description', 
            'quantity', 
            'price', 
            'location', 
            'availability_date', 
            'unit', 
            'status', 
            'created_at', 
            'updated_at',
            'photos'
        ]