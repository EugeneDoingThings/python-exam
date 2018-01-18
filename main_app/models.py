import uuid
from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    email = models.CharField(max_length=150)
    fullname = models.CharField(max_length=150)
    password = models.CharField(max_length=150)


class Product(models.Model):
    name = models.CharField(max_length=150)
    category = models.CharField(max_length=50)


class ProductVersion(models.Model):
    link = models.ForeignKey(Product, related_name='product')


class Order(models.Model):
    name = models.ForeignKey(User, related_name='orders')
    delivery_address = models.CharField(max_length=150)
    delivery_date = models.DateTimeField(auto_now=False, auto_now_add=False)
