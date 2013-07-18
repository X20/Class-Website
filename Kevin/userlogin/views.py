# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Permission, Group
from django.template import RequestContext

usernameList = User.objects.all();

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

def toRegister(request):
	c={}
	c.update(csrf(request))
	return render_to_response('register.html', c, context_instance=RequestContext(request))

def checkUsername (a):
    if len(a) >20:
        return False
    for i in range(0,len(a)):
        p = ord(a[i])
        if p > 122 or ( p < 97 and p > 90) or (p < 65 and p > 57) or p < 48:
            if p != 95:
                return False
    return True

def checkPassword (a):
    if len(a) < 6 or len(a) > 30:
        return False
    return True

def checkEmail (a):
    js = 0
    for i in range(0, len(a)):
        if a[i] == '@':
            js+=1
    if js == 1:
        return True
    return False


def register(request):
    #return HttpResponse("page incomplete")
    c={}
    newUsername=request.POST.get('newUsername', '')
    password=request.POST.get('password', '')
    confirmpassword=request.POST.get('confirmpassword', '')
    email=request.POST.get('email', '')
    if usernameList.filter(username=newUsername):
        c['warning'] = "Username already registered!"
        return render_to_response('register.html', c, context_instance=RequestContext(request))
    elif not newUsername or not password or not confirmpassword:
        c['warning'] = "Username or password is blank!"
        return render_to_response('register.html', c, context_instance=RequestContext(request))
    elif password != confirmpassword:
        c['warning'] = "Confirming pasword is different from password!"
        return render_to_response('register.html', c, context_instance=RequestContext(request))
    elif not checkUsername (newUsername):
        c['warning'] = "Invalid username!"
        return render_to_response('register.html', c, context_instance=RequestContext(request))
    elif not checkPassword (password):
        c['warning'] = "Invalid password!"
        return render_to_response('register.html', c, context_instance=RequestContext(request))
    elif not checkEmail (email):
        c['warning'] = "Invalid email address!"
        return render_to_response('register.html', c, context_instance=RequestContext(request))
    else:
        user=User.objects.create_user(username=newUsername, email=email, password=password)
        user.save()
		# userGroup=UserGroup.objects.create(username=user.username)
		# userGroup.save()
        return HttpResponseRedirect('/')

############ QuoteEnd ##########################
