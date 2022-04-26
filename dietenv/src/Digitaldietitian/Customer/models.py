import email
from pyexpat import model
from sys import maxsize
from django.db import models
from django.forms import FloatField, PasswordInput
from django.contrib.auth.models import AbstractUser

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
    ERName=models.CharField(blank=False,null=False,max_length=20)
    dateRegistered=models.DateTimeField(auto_now=True)

class HealthyStatus(models.Model):
    HSId=models.AutoField(primary_key=True)
    HSName=models.CharField(blank=False,null=False,max_length=50)
    dateRegistered=models.DateTimeField(auto_now=True)

class Diseases(models.Model):
    DId=models.AutoField(primary_key=True)
    DName=models.CharField(blank=False,null=False,max_length=50)
    dateRegistered=models.DateTimeField(auto_now=True)

class User(AbstractUser):
    customerID=models.CharField(unique=True,max_length=20,null=False,blank=False)
    email=models.EmailField(primary_key=True)
    phoneno=models.CharField(null=False, blank=False, unique=True,max_length=12)
    customerName=models.CharField(null=False,blank=False,max_length=60)
    role=models.ForeignKey(Role, on_delete=models.CASCADE)
    age=models.IntegerField(null=False,blank=False)
    height=models.DecimalField(max_digits=2,decimal_places=2 ,blank=False,null=False)
    weight=models.DecimalField(max_digits=3,decimal_places=2 ,blank=False,null=False)
    exercising=models.ForeignKey(ExercisingRate, on_delete=models.CASCADE)
    disease = models.ForeignKey(Diseases, on_delete=models.CASCADE)
    healthStatus=models.ForeignKey(HealthyStatus, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    dateRegistered=models.DateTimeField(auto_now=True)
    password=models.CharField(max_length=100,null=False,blank=False)

    class Meta:
        permissions = [
            ("change_details", "See diet plan"),
            ("close_app", "Can chat with dietitian"),
        ]

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