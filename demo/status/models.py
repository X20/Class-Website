from django.db import models

from userlogin.models import Group

class Headup(models.Model):
	groupContext=models.ForeignKey(Group)
	sender=models.CharField(max_length=30)
	time=models.DateTimeField(auto_now=True)
	content=models.TextField(max_length=140)