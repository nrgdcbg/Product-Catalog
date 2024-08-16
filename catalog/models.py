from distutils.command.build_scripts import first_line_re
from email.headerregistry import Address
from itertools import product
from pickle import TRUE
from pyexpat import model
from tokenize import Name
from typing import KeysView
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class AuthUser(AbstractUser):
    USER_TYPE_CHOICES = {
        (1, 'Product Manager'),
        (2, 'Customer'),
        (3, 'Customer Manager'),
        (4, 'Reviewer'),
    }
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES,null=True)

class ProductManager(models.Model):
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE, null=True)
    profilepicture=models.ImageField(null=True, blank=True, upload_to = '', default='default_pfp.png')

class Supplier(models.Model):
    name=models.CharField(max_length=200,null=TRUE)
    address=models.CharField(max_length=200,null=TRUE)
    email=models.CharField(max_length=200,null=TRUE)
    telephone=models.CharField(max_length=200,null=TRUE)
    contactperson=models.CharField(max_length=200, null=TRUE)
    isarchived=models.BooleanField(default=False)
    displaypicture = models.ImageField(null=True, blank=True, upload_to = 'suppliers', default='/default_pfp.png')

    def __str__(self):
        return self.name

class Catalog(models.Model):
    details = models.TextField()

class Reviewer(models.Model):
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE, null=True)
    name=models.CharField(max_length=200,null=True)
    address = models.CharField(max_length=200,null=True)
    profilepicture = models.ImageField(null=True, blank=True, upload_to = '', default='/default_pfp.png')
    contact = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=200,null=True)
    description=models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name=models.CharField(max_length=200,null=True)
    rating = models.FloatField(default=True)
    description = models.TextField(blank=True, null=True)
    stocks = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    reorderlvl = models.IntegerField(validators=[MinValueValidator(0)])
    sellingprice = models.FloatField(validators=[MinValueValidator(0)])
    discount = models.FloatField(validators=[MinValueValidator(0)])
    isarchived = models.BooleanField(default=False)
    isFeatured = models.BooleanField(default=False)

    @property
    def getRatings(self):
        reviews = list(self.review_set.all().values_list('rating'))
        keys = [1, 2, 3, 4, 5]
        values = []

        r = []
        for x in reviews:
            r.append(x[0])
    
        for key in keys:
            values.append(r.count(key))
                
        ratings = dict(zip(keys, values))

        return ratings

    def __str__(self):
        return self.name

class SupplierProduct(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    supplier=models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)
    leadtime = models.IntegerField(null=True, validators=[MinValueValidator(0)])
    supplierprice=models.FloatField(validators=[MinValueValidator(0)])
    discount = models.FloatField(validators=[MinValueValidator(0)])
    isarchived = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product}"

class ProductCatalog(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    catalog=models.ForeignKey(Catalog, on_delete=models.CASCADE)
    details=models.TextField(blank=True,null=True)
    joindate=models.DateTimeField(auto_now_add=True)

class ProductPhotos(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE, null = True, related_name='photos')
    photo= models.ImageField(upload_to='images',null=True)

class ProductVideos(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE, null = True, related_name='videos')
    media= models.FileField(upload_to='videos',null=True)

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE)
    details = models.TextField(blank=True, null=True)
    rating = models.FloatField(null=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    date = models.DateTimeField(auto_now_add=True)