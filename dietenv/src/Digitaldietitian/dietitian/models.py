from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from .managers import UserManager

class Zone(models.Model):
    zoneId=models.AutoField(primary_key=True)
    zoneName=models.CharField(blank=False,null=False,max_length=50)
    dateRegistered=models.DateTimeField(auto_now=True)

class Region(models.Model):
    regionId=models.AutoField(primary_key=True)
    regionName=models.CharField(blank=False,null=False,max_length=20)
    zone=models.ForeignKey('Zone', on_delete=models.CASCADE)
    dateRegistered=models.DateTimeField(auto_now=True)

class MealtimeName(models.Model):
    mtId=models.AutoField(primary_key=True)
    mtName=models.CharField(blank=False,null=False,max_length=50)
    dateRegistered=models.DateTimeField(auto_now=True)

class ExercisingRate(models.Model):
    ERId=models.AutoField(primary_key=True)
    ERName=models.CharField(blank=False,null=False,max_length=60)
    dateRegistered=models.DateTimeField(auto_now=True)

class HealthyStatus(models.Model):
    HSId=models.AutoField(primary_key=True)
    HSName=models.CharField(blank=False,null=False,max_length=50)
    dateRegistered=models.DateTimeField(auto_now=True)

class Diseases(models.Model):
    DId=models.AutoField(primary_key=True)
    DName=models.CharField(blank=False,null=False,max_length=50)
    dateRegistered=models.DateTimeField(auto_now=True)

class User(AbstractBaseUser):
    username=models.CharField(unique=True,max_length=50)
    first_name=models.CharField(unique=True,max_length=50)
    last_name=models.CharField(unique=True,max_length=50)
    email=models.EmailField(primary_key=True)
    phoneno=models.CharField(null=False, blank=False, unique=True,max_length=12)
    age=models.IntegerField(null=False,blank=False)
    region = models.ForeignKey(Region, on_delete=models.DO_NOTHING,null=True,blank=True)
    dateRegistered=models.DateTimeField(auto_now=True)
    password=models.CharField(max_length=1000,null=False,blank=False)
    is_active = models.BooleanField(_('active'), default=True)
    is_superuser=models.BooleanField(_('superuser'), default=True)
    is_staff=models.BooleanField(_('staff'),default=True)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    class Meta:
        app_label='dietitian'
        ordering = ('username',)

    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','phoneno','age','password']

class FoodData(models.Model):
    name=models.CharField(primary_key=True, max_length=200)	
    ash=models.DecimalField(max_digits=6,decimal_places=2,blank=True,null=True)
    carbohydrate=models.DecimalField(max_digits=6,decimal_places=2,blank=True,null=True)		
    fiber=models.DecimalField(max_digits=6,decimal_places=2,blank=True,null=True)			
    sugarTotal=models.DecimalField(max_digits=6,decimal_places=2,blank=True,null=True)	
    water=models.DecimalField(max_digits=6,decimal_places=2,blank=True,null=True)	
    monosaturatedFat=models.DecimalField(max_digits=6,decimal_places=2,blank=True,null=True)	
    polysaturatedFat=models.DecimalField(max_digits=6,decimal_places=2,blank=True,null=True)	
    saturatedFat=models.DecimalField(max_digits=6,decimal_places=2,blank=True,null=True)
    totalLipid=models.DecimalField(max_digits=6,decimal_places=2,blank=True,null=True)	
    vitamin_A_IU=models.DecimalField(max_digits=6,decimal_places=2,blank=True,null=True)
    vitamin_A_RAE=models.DecimalField(max_digits=6,decimal_places=2,blank=True,null=True)	
    vitamin_B12=models.DecimalField(max_digits=6,decimal_places=2,blank=True,null=True)	
    vitamin_B6=models.DecimalField(max_digits=6,decimal_places=2,blank=True,null=True)	
    vitamin_C=models.DecimalField(max_digits=6,decimal_places=2,blank=True,null=True)	
    vitamin_E=models.DecimalField(max_digits=6,decimal_places=2,blank=True,null=True)
    vitamin_K=models.DecimalField(max_digits=6,decimal_places=2,blank=True,null=True)	
    mineralsCalcium=models.DecimalField(max_digits=6,decimal_places=2,blank=True,null=True)	
    mineralsIron=models.DecimalField(max_digits=6,decimal_places=2,blank=True,null=True)	
    mineralsPotassium=models.DecimalField(max_digits=6,decimal_places=2,blank=True,null=True)	
    mineralsSodium=models.DecimalField(max_digits=6,decimal_places=2,blank=True,null=True)
    protein=models.DecimalField(max_digits=6,decimal_places=2,blank=True,null=True)
    cholesterol=models.DecimalField(max_digits=6,decimal_places=2,blank=True,null=True)
    kilocalories=models.DecimalField(max_digits=6,decimal_places=2,blank=True,null=True)
    dateRegistered=models.DateTimeField(auto_now=True)
    mealTime=models.ManyToManyField(MealtimeName,swappable=True,unique=False)