from django.db import models
from userlogin.models import Group
from django.contrib.auth.models import User
# Create your models here. file

class GroupFile(models.Model):
	group=models.ForeignKey(Group)
	file=models.FileField(upload_to='media/')
	filename=models.CharField(max_length=50)
	uploadTime=models.DateTimeField(auto_now=True)
	sender=models.ForeignKey(User)
	
	def __unicode__(self):
		return self.filename