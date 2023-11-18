from django.db import models
from django.contrib.auth.models import User

# Create your models here. pascal case
class Category(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        verbose_name_plural = 'Categories' ##akahe s katanor jonno meta class use kora hoi
    def __str__(self):
        ordering = ['name']
        return self.name   
class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    created_at = models.DateField(auto_now_add=True)  # Updated field name
    image = models.ImageField(upload_to='product_images', blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    is_sold = models.BooleanField(default=False)

    def __str__(self):
        return self.name

