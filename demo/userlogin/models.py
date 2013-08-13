from django.db import models
from django.contrib.auth.models import User
#create your models here. userlogin

class MyHead(models.Model):
	user=models.OneToOneField(User)
	headImg=models.ImageField(upload_to='media/')
	imgName=models.CharField(max_length=30)

class Group(models.Model):
	groupName=models.CharField(max_length=50)
	note=models.TextField(max_length=100)
	memberList=models.ManyToManyField(User)
	#status=models.CharField(max_length=50)
