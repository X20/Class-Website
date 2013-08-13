# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from messege.models import Group, chat
from userlogin import Group
from messege.models import Chat
from django.db.models import Q
from decorators.decorator import authen

import json

#the expansion of namelist within one particular group
allGroup=Group.objects.all()

def messegePage(request):
	groupSet=request.user.group_set
	groupList=[index.groupName for index in groupSet]
	return render_to_response('messege.html', {'user': request.user, 'groupList': groupList})

def expandNameList(request):
	#pass
	clickedName=request.POST.get('groupName', '')
	selectedGroup=allGroup.get(groupName=clickedName)
	friendset=selectedGroup.memberList
	friendNameList=[cursor.username for cursor in friendset]
	return json.dumps(friendNameList)

recordEntry=7
def clickName(request):
	thisFriend=request.POST.get('clickName', '')
	allChatRecord=Chat.objects.filter(
		(Q(sender=thisFriend, reciever=request.user.username)|
		Q(sender=request.user.username, reciever=thisFriend))
	)
	chatRecord=allCharRecord.order_by('time')[:recordEntry]
	recordList=[(entry.sender+r": "+entry.content+r'\n'+entry.time) for entry in chatRecord]
	return json.dumps(recordList)
	
def chitchat(request):
	#pass
	friendName=request.POST.get('friendName', '')
	content=request.POST.get('content', '')
	newChatRecord=Chat(sender=request.user.username, reciever=friendName, content=content)
	newChatRecord.save()
	tmpStr=newChatRecord.sender+r': '+newChatRecord.content+r'\n'+newChatRecord.time
	return json.dumps([tmpStr.decode()])
	