# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Permission, Group
from django.template import RequestContext

def userlogin(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/home/')
    username, password = request.POST["user"], request.POST["pass"]
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/home/')
    else:
        c = {}
        c.update(csrf(request))
        return render_to_response('indexw.html', c, context_instance=RequestContext(request))

def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/')

def index(request):
    c = {}
    c.update(csrf(request))
    if request.user.is_authenticated():
        return HttpResponseRedirect('/home/')
    else:
        return render_to_response('index.html', c, context_instance=RequestContext(request))

def home(request):
    c = {}
    if request.user.is_authenticated():
        c['name'] = request.user.username
        return render_to_response('home.html', c, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/')


############# Quote zhazhazhang ###############

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

############ QuoteEnd ##########################
