# Create your views here.
from django.http import HttpResponse #, HttpResponseRedirect
from status.models import Headup
from userlogin import Group
from django.contrib.auth.models import User

import json

statusNumber=10

def statusPage(request):
	return render_to_response('messege.html', {'user': request.user})

def expandFriendList(request):
	groupSet=request.user.group_set.all()
	friendList=[]
	for index in groupSet:
		friendList+=[entry.username for entry in index.memberList]
	return json.dumps(friendList)
	
def expandGroupList(request):
	groupSet=request.user.group_set.all()
	groupList=[index.groupName for index in groupSet]
	return json.dumps(groupList)
	
def showGroupStatus(request):
	groupName=request.POST.get('groupName', '')
	groupChosen=Group.objecs.get(groupName=groupName)
	statusSet=groupChosen.headup_set.all().order_by('time')
	allRecordList=[{'sender': entry.sender, 'content': entry.content, 'time': entry.time} for entry in statusSet]
	recordList=allRecordList[:statusNumber]
	return json.dumps(recordList)
	
def headup(request):
	groupName=request.POST.get('groupName', '')
	thisGroup=Group.objects.get(groupName=groupName)
	
	senderName=request.user.username
	content=request.POST.get('content', '')
	newHeadup=Headup(content=content, sender=senderName)
	newHeadup.save()
	thisGroup.headup_set.all().add(newHeadup)
	thisGroup.save()
	
	#tmpStr=senderName+r': '+content+r'\n'+newHeadup.time
	recordList=[{'sender': senderName, 'content': content, 'time': newHeadup.time}]
	return json.dumps(recordList)

def iterBiList(biList):
	for i in biList:
		for j in i:
			yield j
	
def filterCheck(request):
	#filterFunction=json.loads(request.POST.get('filterFunction', ''))
	filterFriend=json.loads(request.POST.get('filterFriend', ''))
	filterGroup=json.loads(request.POST.get('filterGroup', ''))

	#checking invalid group selection
	me=request.user
	myGroup=[i.groupName for i in me.group_set.all()]
	for i in filterGroup:
		if not i in myGroup:
			filterGroup.remove(i)
	
	groupList=[Group.objects.get(groupName=i).headup_set.all() for i in filterGroup]
	
	statusList=[{'content': i.content, 'sender': i.sender, 'time': i.time} for i in iterBiList(groupList) if i.sender in filterFriend]
	
	return json.dumps(statusList)