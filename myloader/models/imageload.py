from django.db import models
from myloader.models.category import Category


class MyImage(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='images/')
