from dataclasses import field
from datetime import timedelta
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from numpy import mod
from dietitian.models import *
from phonenumber_field.modelfields import PhoneNumberField

def nameFile(instance, filename):
    return '/'.join(['images', str(instance.customerName), filename])

class Customer(models.Model):
    # userimage=models.ImageField(upload_to=nameFile,default='defimg.png')
    customerID=models.CharField(unique=True,max_length=20,null=False,blank=False)
    email=models.EmailField(primary_key=True)
    phoneno=PhoneNumberField()
    customerName=models.CharField(null=False,blank=False,max_length=60)
    age=models.IntegerField(null=False,blank=False)
    height=models.DecimalField(max_digits=3,decimal_places=2 ,blank=False,null=False)
    weight=models.DecimalField(max_digits=4,decimal_places=2 ,blank=False,null=False)
    exercising=models.ForeignKey(ExercisingRate, on_delete=models.CASCADE,default=None)
    disease = models.ForeignKey(Diseases, on_delete=models.CASCADE,default=None)
    healthStatus=models.ForeignKey(HealthyStatus, on_delete=models.CASCADE,default=None)
    region = models.ForeignKey(Region, on_delete=models.CASCADE,default=None)
    dateRegistered=models.DateTimeField(auto_now=True)
    password=models.CharField(max_length=100,null=False,blank=False)
    is_active = models.BooleanField(_('active'), default=True)
    lastlogin=models.CharField(max_length=100,default=(datetime.today().date()-timedelta(days=1)))

    class Meta:
        ordering = ('email',)

    
class MealAssigned(models.Model):
    mealTime=models.ForeignKey(MealtimeName, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    food=models.ForeignKey(FoodData, on_delete=models.CASCADE,default=None)
    dateofentry=models.DateField(auto_now=False, auto_now_add=True)
