from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Unit_Of_Measure(models.Model):
    measure = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.measure

     
class Item_Group(models.Model):
    item_group_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.item_group_name

 
class Item(models.Model):
    item_name = models.CharField(max_length=150)
    unit_of_measure = models.ForeignKey(Unit_Of_Measure, on_delete=models.CASCADE)
    item_group = models.ForeignKey(Item_Group, on_delete=models.CASCADE)

 
class Note(models.Model):
    content = models.TextField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
 
     
class Year(models.Model):
    year = models.IntegerField()
    locked = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.year)

 
class Plan(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    qty = models.IntegerField()
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(default=timezone.now)


class Center(models.Model):
    center_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.center_name


class Center_Item_Group(models.Model):
    center = models.ForeignKey(Center, on_delete=models.CASCADE)
    item_group = models.ForeignKey(Item_Group, on_delete=models.CASCADE)

    
class User_Center(models.Model):
    center = models.ForeignKey(Center, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.user) + " - " + str(self.center)