# Create your views here.
from django.core.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group, Permission
from userlogin.models import Group
from userlogin.views import handleUploadedImage

import os

def home(request):
	c={}
	c.update(csrf(request))

	if not request.user.is_authenticated():
		return HttpResponseRedirect('/')
	
	#mending
	newHeadImgName=request.FILES['newFace'].name
	if newHeadImgName:
		request.user.myhead.delete()
		
		#removing the former image file
		curImg=r'media/'+request.user.username+r'/'+request.user.myhead.imgName
		os.remove(curImg)
		
		#binding with new image file
		newHeadImg=request.FILES['img']
		newImage=MyHead(user=request.user, headImg=newHeadImg, imgName=newHeadImgName)
		handleUploadedImage(newHeadImg, newHeadImgName, request.user.username)
	
	dic={'jsURL': "/static/home.js" ,'username': request.user.username}
	dic['img']=r'media/'+request.user.username+r'/'+request.user.myhead.imgName
	
	c.update(dic)
	
	return render_to_response('homepage.html', c)

def allGroup(request):
	c={}
	c.update(csrf(request))
	
	newgroupname=request.POST.get('newGroup', '')
	note=request.POST.get('note', '')
	
	#me=userQuerySet.get(username=request.user.username)
	me=request.user
	
	if newgroupname:
		groupQuerySet=Group.objects.all()
		
		#mending
		newGroup=Group(groupName=newgroupname, note=note)
		newGroup.save()
		newGroup.memberList.add(me)
		newGroup.save()
		
		os.makedirs('media/'+newgroupname+'/')
		
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
	
	myGroup=me.group_set.all()
	
	dic={'username': request.user.username, 'allGroup': Group.objects.all(), 'myGroup': myGroup}
	
	c.update(dic)
	return render_to_response('group.html', c)