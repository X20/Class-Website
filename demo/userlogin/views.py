# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group, Permission
from userlogin.models import UserGroup

usernameList=User.objects.all()

def index(request):
	c={}
	c.update(csrf(request))
	return render_to_response('form.html', c)

def userLogin(request):
	#return HttpResponse("login incomplete")
	
	username=request.POST.get('username', '')
	password=request.POST.get('password', '')
	if not username:
		return HttpResponseRedirect("/")
	user=authenticate(username=username, password=password)
	if user is not None:
		login(request, user)
		return HttpResponseRedirect("/homepage/")
		#return render_to_response("homepage.html", {'username': username})
 	
	else:
		return HttpResponseRedirect("/")
	
def toRegister(request):
	c={}
	c.update(csrf(request))
	return render_to_response('register.html', c)
	
def register(request):
	#return HttpResponse("page incomplete")
	newUsername=request.POST.get('newUsername', '')
	password=request.POST.get('password', '')
	email=request.POST.get('email', '')
	if usernameList.filter(username=newUsername):
		return HttpResponseRedirect('/toRegister/')
	elif not newUsername or not password:
		return HttpResponseRedirect('/toRegister/')
	else:
		user=User.objects.create_user(username=newUsername, email=email, password=password)
		user.save()
		userGroup=UserGroup.objects.create(username=user.username)
		userGroup.save()
		return HttpResponseRedirect('/')
		
def userLogout(request):
	#return HttpResponse("logout incomplete")
	logout(request)
	return HttpResponseRedirect("/")
	
def valid(request):
	return HttpResponse("valid incomplete")
	