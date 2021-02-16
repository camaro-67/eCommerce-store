from django.shortcuts import render
from django.db import models
# Create your views here.
class Product(models.Model):
    p_desc = models.CharField(max_length=254, default=True)
    p_name = models.CharField(max_length=254,default=True)
    p_price =  models.DecimalField(max_digits=10, decimal_places=2,default=True)
    slug = models.SlugField(max_length=200, default=True)
    p_image = models.ImageField(default=False)
    p_latest_img = models.ImageField(default=False)