from django.db import models
from django.contrib.auth.models import User

SIZES = (('XS', 'Extra-Small'), ('S', 'Small'), ('M', 'Medium'),
         ('L', 'Large'), ('XL', 'Extra-Large'))

SHOESIZES = (('6', 'Six'), ('7', 'Seven'), ('8', 'Eight'), ('9', 'Nine'),
             ('10', 'Ten'), ('11', 'Eleven'))


# Create your models here.
class Shoe(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    shoe_size = models.CharField(max_length=2,
                                 choices=SHOESIZES,
                                 default=SHOESIZES[2][0])
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name


class Clothing(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    size = models.CharField(max_length=2, choices=SIZES, default=SIZES[1][0])
    description = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shoes = models.ManyToManyField(Shoe)

    def __str__(self):
        return f"{self.get_size_display()} on {self.name}"


class Photo(models.Model):
    url = models.CharField(max_length=200)
    clothing = models.ForeignKey(Clothing, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for clothing_id: {self.clothing_id} @{self.url}"