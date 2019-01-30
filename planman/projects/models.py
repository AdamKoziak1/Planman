from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200,default = 'Untitled project ',blank=True)
    owner = models.ForeignKey(User,on_delete=models.SET_NULL,null = True)
    description = models.TextField(null=True,blank=True,default = 'description')
    cost = models.DecimalField(max_digits=19,decimal_places=2,null=True,blank=True,default=0)
    profit = models.DecimalField(max_digits=19,decimal_places=2,null=True,blank=True,default=0)
    start_date = models.DateField(null=True,blank=True)
    end_date = models.DateField(null=True,blank=True)
    def __str__(self):
        return self.name
    

class Task(models.Model):
    name = models.CharField(max_length=200,default = 'Untitled task ',blank=True)
    description = models.TextField(null=True,blank=True,default = 'description')
    cost = models.DecimalField(max_digits=19,decimal_places=2,null=True,blank=True,default=0)
    profit = models.DecimalField(max_digits=19,decimal_places=2,null=True,blank=True,default=0)
    start_date = models.DateField(null=True,blank=True)
    end_date = models.DateField(null=True,blank=True)
    hours_to_finish = models.IntegerField(null=True,blank=True,default=0)
    hours_finished = models.IntegerField(null=True,blank=True,default=0)
    project= models.ForeignKey(Project,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Project_members(models.Model):
    users = models.ManyToManyField(User)
    project= models.ForeignKey(Project,on_delete=models.CASCADE)

