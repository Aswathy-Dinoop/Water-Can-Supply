from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserType(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    type=models.CharField(max_length=10,null=True)
class Registration(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=50,null=True)
    phone=models.CharField(max_length=50,null=True)
    address=models.CharField(max_length=50,null=True)
    district=models.CharField(max_length=50,null=True)
    password=models.CharField(max_length=50,null=True)
class AddCompany(models.Model):
    companyname=models.CharField(max_length=50,null=True)
    logo=models.ImageField(null=True)
class Products(models.Model):
    companyname=models.ForeignKey(AddCompany,on_delete=models.CASCADE,null=True)
    size=models.CharField(max_length=20,null=True)
    price=models.CharField(max_length=25,null=True)
    total_quantity=models.CharField(max_length=5000)
    image=models.ImageField(null=True)
class AddtoCart(models.Model):
    products=models.ForeignKey(Products,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(Registration,on_delete=models.CASCADE,null=True)
    company=models.ForeignKey(AddCompany,on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to='media/',null=True)
    price=models.CharField(max_length=150,null=True)
    quantity=models.CharField(max_length=150,null=True)
    status=models.CharField(max_length=150,null=True)
    payment=models.CharField(max_length=150,null=True)
