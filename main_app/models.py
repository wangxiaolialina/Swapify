from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

SIZES = (('XS', 'Extra-Small'), ('S', 'Small'), ('M', 'Medium'),
         ('L', 'Large'), ('XL', 'Extra-Large'))

SHOESIZES = (('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'),
             ('10', '10'), ('11', '11'), ('12','12'))


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
    url = models.CharField(max_length=200, blank = True)

    def get_photo(self):
        return f"Photo for shoe_id: {self.shoe_id} @{self.url}"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shoes_detail', kwargs={'shoe_id': self.id})


class Clothing(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    size = models.CharField(max_length=2, choices=SIZES, default=SIZES[1][0])
    description = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shoes = models.ManyToManyField(Shoe, blank = True)
    url = models.CharField(max_length=200, blank = True)


    def get_photo(self):
        return f"Photo for clothing_id: {self.clothing_id} @{self.url}"



    def __str__(self):
        return f"{self.name} - Size {self.get_size_display()}"

    def get_absolute_url(self):
        return reverse('detail', kwargs={'clothing_id': self.id})

