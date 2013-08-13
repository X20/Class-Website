from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group, Permission
from django.http import HttpRespnse, HttpResponseRedirect
from django.shortcute import render_to_response

def authen(func):
	def wrapped(request):
		user=authenticate(username=request.user.username, password=request.user.password)
		if user is None:
			return HttpResponseRedirect("/")
		else:
			func(request)
	return wrapped
	
