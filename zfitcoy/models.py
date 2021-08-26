from django.db import models
from django.contrib.auth.models import User
from djrichtextfield.models import RichTextField


class Blog_category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Blogs(models.Model):
    categorys = models.ForeignKey(Blog_category, on_delete=models.CASCADE, null=True)
    name =  models.CharField(max_length=50)
    detail = RichTextField(null=True)
    image = models.FileField(null=True)
    date = models.DateField(auto_now=True)
    def __str__(self):
        return self.name

class Team(models.Model):
    name =  models.CharField(null=True,max_length=50)
    post =  models.CharField(null=True,max_length=50)
    detail = RichTextField(null=True)
    image = models.FileField(null=True)
    date = models.DateField(auto_now=True)
    def __str__(self):
        return self.name

class Services(models.Model):
    name =  models.CharField(null=True,max_length=50)
    detail = models.CharField(null=True,max_length=100)
    discription = RichTextField(null=True)
    image = models.FileField(null=True)
    Logo = models.FileField(null=True)
    date = models.DateField(auto_now=True)
    def __str__(self):
        return self.name