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

def message(request):
    c = {}
    if request.user.is_authenticated():
        c['name'] = request.user.username
        c['friends'] = User.objects.all()
        return render_to_response('message.html', c, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/')

