from django.db import models

class ProductListing(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('sold', 'Sold'),
        ('expired', 'Expired'),
    ]
    UNIT_CHOICES = [
        ('kg', 'Kilogram'),
        ('bunch', 'Bunch'),
        ('crate', 'Crate'),
        ('dozen', 'Dozen'),
        ('litre', 'Litre'),
        ('piece', 'Piece'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    availability_date = models.DateField()
    unit = models.CharField(max_length=20, choices=UNIT_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ProductPhoto(models.Model):
    product = models.ForeignKey(ProductListing, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)