# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from userlogin.models import Group, UserGroup
from status.models import Headup

import json

userlist=UserGroup.objects.all()
grouplist=Group.objects.all()

def handle_uploaded_file(file, filename, groupName):
    with open('media/'+groupName+'/'+filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

def handle_download_file(fn, buf_size=262144):
	with open(fn, 'rb') as f:
		while True:
			c=f.read(buf_size)
			if c:
				yield c
			else:
				break
			
def clickGroup(request):
	thisGroup=request.POST.get('groupName', '')
	groupFile=thisGroup.file_set.all().order_by('uploadTime')
	fileRecord=[{'sender': entry.sender, 'file': entry.filename, 'time': entry.uploadTime} for entry in groupFile]
	return json.dumps(fileRecord)
	
def upload(request):
	c={}
	c.update(csrf(request))
	
	groupName=request.POST.get('groupName', '')
	filename=request.POST.get('filename', '')
	thisGroup=groupList.get(groupName=groupName)
	
	if request.method == 'POST':
		form = UploadFile(filename=filename, file=request.FILES['file'], group=thisGroup)
		#if form.is_valid():
		handle_uploaded_file(request.FILES['file'], filename, groupName)
		form.save()
		
		groupStatus=Headup(groupContext=thisGroup, sender=request.user.username, content=sender+' uploaded '+filename)
		groupStatus.save()
		
		return HttpResponseRedirect('/file/')

def download(request):
	dic=json.loads(request.POST.get('downloadInfo'))
	
	filename=dic.filename
	groupName=dic.groupName
	fn='media/'+groupName+'/'+filename
	
	response=HttpResponse(readFile(fn))
	return response
	
def showPage(request):
	c={}
	c.update(csrf(request))
	
	myGroup=request.user.group_set.all()
	myGroupList=[single.groupName for single in myGroup]
	
	c['myGroupList']=myGroupList
	
	return render_to_response('file.html', c)
