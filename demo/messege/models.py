from django.db import models
from userlogin.models import Group

# Create your models here.

class chat(models.Model):
	sender=models.CharField(max_length=30)
	reciever=models.CharField(max_length=30)
	content=models.TextField(max_length=140)
	time=models.DateTimeField(auto_now=True)