import email
from pyexpat import model
from sys import maxsize
from django.db import models
from django.forms import FloatField
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
    zone=models.ForeignKey('Zone',related_name='zoneId', on_delete=models.CASCADE)
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
    role=models.ForeignKey('Role', related_name='roleID', on_delete=models.CASCADE)
    age=models.IntegerField(max_length=3,null=False,blank=False)
    height=models.DecimalField(max_digits=2,decimal_places=2 ,blank=False,null=False)
    weight=models.DecimalField(max_digits=3,decimal_places=2 ,blank=False,null=False)
    exercising=models.ForeignKey("ExercisingRate", related_name='ERId', on_delete=models.CASCADE)
    disease = models.ForeignKey(Diseases, on_delete=models.CASCADE)
    healthStatus=models.ForeignKey(HealthyStatus,related_name='HSId', on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    dateRegistered=models.DateTimeField(auto_now=True)

class Food(models.Model):
    pass