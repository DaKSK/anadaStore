from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255)
    in_stock = models.BooleanField(default=True)  # Stock to change to numeric value
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def __str__(self):
        return self.title


# Purchases
class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


# Profile
# class Profile(models.Model):
#
#     # Managed fields
#     user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
#     phone = models.CharField(max_length=32, null=True, blank=True)
#     address = models.CharField(max_length=255, null=True, blank=True)
#     city = models.CharField(max_length=50, null=True, blank=True)
#     purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
