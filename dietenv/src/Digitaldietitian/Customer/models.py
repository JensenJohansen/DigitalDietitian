from dataclasses import field
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from dietitian.models import *


class Customer(models.Model):
    customerID=models.CharField(unique=True,max_length=20,null=False,blank=False)
    email=models.EmailField(primary_key=True)
    phoneno=models.CharField(null=False, blank=False, unique=True,max_length=12)
    customerName=models.CharField(null=False,blank=False,max_length=60)
    role=models.ForeignKey(Role, on_delete=models.CASCADE,default=None)
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

    class Meta:
        ordering = ('email',)

    
class MealAssigned(models.Model):
    mealTime=models.ForeignKey(MealtimeName, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    food=models.ForeignKey(FoodData, on_delete=models.CASCADE,default=None)
    dateofentry=models.DateTimeField(auto_now=True, auto_now_add=False)
