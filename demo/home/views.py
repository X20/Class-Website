# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group, Permission
from userlogin.models import Group

import os

def home(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/')
	return render_to_response('homepage.html', {'jsURL': "/static/home.js" ,'username': request.user.username})

#userQuerySet=UserGroup.objects.all()
	
def allGroup(request):
	newgroupname=request.POST.get('newGroup', '')
	note=request.POST.get('note', '')
	
	#me=userQuerySet.get(username=request.user.username)
	me=request.user
	
	if newgroupname:
		groupQuerySet=Group.objects.all()
		newGroup=Group(groupName=newgroupname, note=note)
		newGroup.memberList.add(me)
		newGroup.save()
		
		os.makedirs('media/'+newgroupname+'/')
		
		#me=userQuerySet.get(username=request.user.username)
		#newGroup.usergroup_set.add(me)
		me.group_set.add(newGroup)
		#newGroup.save()
		me.save()
	
	joinGroupName=request.POST.get('join', '')
	if joinGroupName:
		groupQuerySet=Group.objects.all()
		joinGroup=groupQuerySet.get(groupName=joinGroupName)
		#me=userQuerySet.get(uername=request.user.username)
		me.group_set.add(joinGroup)
		me.save()
	
	myGroup=me.group_set
	
	return render_to_reponse('group.html', {'username': request.user.username, 'allGroup': Group.objects.all(), 'myGroup': myGroup})