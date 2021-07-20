from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField(auto_now_add=False,auto_now=False,blank=True)
    priority = models.IntegerField(blank=True,default=1,null=True,validators=[MaxValueValidator(10), MinValueValidator(0)])


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['user','complete','-priority','date']
