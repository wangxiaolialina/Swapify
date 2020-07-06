from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

SIZES = (('XS', 'Extra-Small'), ('S', 'Small'), ('M', 'Medium'),
         ('L', 'Large'), ('XL', 'Extra-Large'))

SHOESIZES = (('6', 'Six'), ('7', 'Seven'), ('8', 'Eight'), ('9', 'Nine'),
             ('10', 'Ten'), ('11', 'Eleven'))


# Create your models here.
class Shoe(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100, blank = True)
    color = models.CharField(max_length=100, blank = True)
    shoe_size = models.CharField(max_length=2,
                                 choices=SHOESIZES,
                                 default=SHOESIZES[2][0])
    description = models.TextField(max_length=250, blank = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shoes_detail', kwargs={'pk': self.id})


class Clothing(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    size = models.CharField(max_length=2, choices=SIZES, default=SIZES[1][0])
    description = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shoes = models.ManyToManyField(Shoe, blank = True )

    def __str__(self):
        return f"{self.name} - Size {self.get_size_display()}"

    def get_absolute_url(self):
        return reverse('detail', kwargs={'clothing_id': self.id})

class Photo(models.Model):
    url = models.CharField(max_length=200)
    clothing = models.ForeignKey(Clothing, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for clothing_id: {self.clothing_id} @{self.url}"