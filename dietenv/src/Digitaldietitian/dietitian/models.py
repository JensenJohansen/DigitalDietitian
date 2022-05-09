from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from .managers import UserManager

class Role(models.Model):
    roleId=models.AutoField(primary_key=True)
    roleName=models.CharField(blank=False,null=False,max_length=20)
    dateRegistered=models.DateTimeField(auto_now=True)

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
    name=models.CharField(primary_key=True, max_length=50)	
    alphaCarotene=models.DecimalField(max_digits=6,decimal_places=2)	
    ash=models.DecimalField(max_digits=6,decimal_places=2)
    betaCarotene=models.DecimalField(max_digits=6,decimal_places=2)	
    betaCryptoxanthin=models.DecimalField(max_digits=6,decimal_places=2)
    carbohydrate=models.DecimalField(max_digits=6,decimal_places=2)	
    cholesterol=models.DecimalField(max_digits=6,decimal_places=2)	
    choline=models.DecimalField(max_digits=6,decimal_places=2)	
    fiber=models.DecimalField(max_digits=6,decimal_places=2)	
    kilocalories=models.DecimalField(max_digits=6,decimal_places=2)	
    luteinAndZeaxanthin=models.DecimalField(max_digits=6,decimal_places=2)	
    lycopene=models.DecimalField(max_digits=6,decimal_places=2)	
    manganese=models.DecimalField(max_digits=6,decimal_places=2)	
    niacin=models.DecimalField(max_digits=6,decimal_places=2)	
    pantothenicAcid=models.DecimalField(max_digits=6,decimal_places=2)
    protein=models.DecimalField(max_digits=6,decimal_places=2)	
    refusePercentage=models.DecimalField(max_digits=6,decimal_places=2)	
    retinol=models.DecimalField(max_digits=6,decimal_places=2)	
    riboflavin=models.DecimalField(max_digits=6,decimal_places=2)	
    selenium=models.DecimalField(max_digits=6,decimal_places=2)	
    sugarTotal=models.DecimalField(max_digits=6,decimal_places=2)	
    thiamin=models.DecimalField(max_digits=6,decimal_places=2)	
    water=models.DecimalField(max_digits=6,decimal_places=2)	
    monosaturatedFat=models.DecimalField(max_digits=6,decimal_places=2)	
    polysaturatedFat=models.DecimalField(max_digits=6,decimal_places=2)	
    saturatedFat=models.DecimalField(max_digits=6,decimal_places=2)
    totalLipid=models.DecimalField(max_digits=6,decimal_places=2)	
    mineralsCalcium=models.DecimalField(max_digits=6,decimal_places=2)	
    mineralsCopper=models.DecimalField(max_digits=6,decimal_places=2)	
    mineralsIron=models.DecimalField(max_digits=6,decimal_places=2)	
    mineralsMagnesium=models.DecimalField(max_digits=6,decimal_places=2)	
    mineralsPhosphorus=models.DecimalField(max_digits=6,decimal_places=2)	
    mineralsPotassium=models.DecimalField(max_digits=6,decimal_places=2)	
    mineralsSodium=models.DecimalField(max_digits=6,decimal_places=2)	
    mineralsZinc=models.DecimalField(max_digits=6,decimal_places=2)	
    vitamin_A_IU=models.DecimalField(max_digits=6,decimal_places=2)
    vitamin_A_RAE=models.DecimalField(max_digits=6,decimal_places=2)	
    vitamin_B12=models.DecimalField(max_digits=6,decimal_places=2)	
    vitamin_B6=models.DecimalField(max_digits=6,decimal_places=2)	
    vitamin_C=models.DecimalField(max_digits=6,decimal_places=2)	
    vitamin_E=models.DecimalField(max_digits=6,decimal_places=2)
    vitamin_K=models.DecimalField(max_digits=6,decimal_places=2)
    amount=models.CharField(max_length=50)
    dateRegistered=models.DateTimeField(auto_now=True)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE,default=None)
    mealTime=models.ManyToManyField(MealtimeName)