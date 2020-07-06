from django.contrib import admin
from .models import Clothing, Shoe, Photo

# Register your models here.
admin.site.register(Clothing)
admin.site.register(Shoe)
admin.site.register(Photo)

