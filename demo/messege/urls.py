from django.conf.urls import patterns, include, url

urlpatterns=patterns('',
	url(r'^$', 'messege,views.messegePage'),
	url(r'^expand/$', 'messege.views.expandNameList'),
	#url(r'^address/$', 'messege.views.addressGroup'),
	url(r'^click/$', 'messege.views.click'),
	url(r'^chat/$', 'messege.views.chitchat'),
)