from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE



# Create your models here.
class User(AbstractUser):
    is_admin = models.BooleanField('is admin', default=False)
    is_employee = models.BooleanField('is employee', default=False)
    
    
    
class Inventory(models.Model):
    Product_Name = models.CharField(max_length= 200, default= None)
    Price = models.FloatField(null=True, default=0.0)
    Availaible_Stock = models.IntegerField(null=True, default=0)
    Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.Product_Name
    
    
class salesRecord(models.Model):
    Transaction_ID = models.CharField(max_length=20, default=None)
    Product_Name = models.CharField(max_length=200, default=None)
    Quantity = models.IntegerField(default=None)
    Price = models.FloatField(default=0.0)
    Date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.Transaction_ID
    
    
    