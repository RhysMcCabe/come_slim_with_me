from django.db import models
import uuid
from django.urls import reverse
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=250, blank=True)
    image = models.ImageField(upload_to='category', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    stock = models.IntegerField()
    color = models.CharField(max_length=20, blank=True)
    image_thumbnail = ImageSpecField(source='image', 
                                        processors=[ResizeToFill(280, 230)], 
                                        format='JPEG', 
                                        options={'quality': 200})

    def __str__(self):
        return self.name

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    descripton = models.TextField(max_length=250, blank=True)
    products = models.ManyToManyField('Product')

    def get_products(self):
        return Product.objects.filter(category=self)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('product_list_by_category',args=[self.id])

