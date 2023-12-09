from django.db import models
from operator import mod
from django.utils import timezone
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import User, Group
from datetime import date

# Create your models here.
class Barangay(models.Model):
    name = models.CharField(max_length = 100)
    healthworker = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name

class Guardian(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    address = models.ForeignKey(Barangay, null=True, on_delete=models.CASCADE)
    contact = models.CharField(max_length=100, null=True)
    # Add additional fields for the guardian profile if needed

    def __str__(self):
        return self.user.username

class Vaccine(models.Model):
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100)
    dose1 = models.BooleanField(null=True)
    dose2 = models.BooleanField(null=True)
    dose3 = models.BooleanField(null=True)
    created = models.DateTimeField(default=timezone.now)
    recommended_age1 = models.CharField(max_length=50, null=True) 
    recommended_age2 = models.CharField(max_length=50, null=True) 
    recommended_age3 = models.CharField(max_length=50, null=True) 

    def __str__(self):
        return self.name

class Register(models.Model):

    child_name = models.CharField(max_length = 100,null=True)       
    date_of_birth = models.DateField(null=True)     
    place_of_birth = models.CharField(max_length = 100,null=True)  
    address = models.ForeignKey(Barangay, null=True, on_delete=models.CASCADE) 
    contact = models.IntegerField(null=True)  
    mother_name = models.CharField(max_length = 100,null=True)       
    father_name = models.CharField(max_length = 100 , null=True)   
    birth_height = models.IntegerField(null=True) 
    birth_weight = models.IntegerField(null=True) 
    sex = models.CharField(max_length = 10, null=True)
    added_by = models.ForeignKey(Guardian, default=None, on_delete=models.CASCADE)
    
    

    def __str__(self):
        return self.child_name

class Vaccine_record(models.Model):
    child = models.ForeignKey(Register, default=None, on_delete=models.CASCADE)
    vaccine_info = models.TextField(default=None)



class Schedule(models.Model):
    child = models.ForeignKey(Register, on_delete=models.SET_NULL, null=True)       
    vax_date = models.DateTimeField(null=True)
    brgy = models.ForeignKey(Barangay, on_delete=models.SET_NULL, null=True)
    guardian = models.ForeignKey(Guardian, default=None, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)
    vaccine_info = models.TextField(default=None)
    def __str__(self):
        return self.child

