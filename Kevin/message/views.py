# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Permission, Group
from django.template import RequestContext

def message(request):
    c = {}
    if request.user.is_authenticated():
        c['name'] = request.user.username
        c['friends'] = User.objects.all().order_by('username')
        return render_to_response('message.html', c, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/')