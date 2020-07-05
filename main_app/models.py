from django.db import models
from django.contrib.auth.models import User

SIZES = (('XS', 'Extra-Small'), ('S', 'Small'), ('M', 'Medium'),
         ('L', 'Large'), ('XL', 'Extra-Large'))


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    size = models.CharField(max_length=2, choices=SIZES, default=SIZES[1][0])
    description = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Photo(models.Model):
    url = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for product_id: {self.product_id} @{self.url}"