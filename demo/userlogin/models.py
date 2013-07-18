from django.db import models
from django.contrib.auth.models import User
#create your models here. userlogin

class Group(models.Model):
	groupName=models.CharField(max_length=50)
	note=models.TextField(max_length=100)
	memberList=models.ManyToManyField(User)
	#status=models.CharField(max_length=50)
