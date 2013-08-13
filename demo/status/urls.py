from django.conf.urls import patterns, include, url

urlpatterns=patterns('',
	url(r'^$', 'status.views.statusPage'),
	url(r'^expandFriendList/$', 'status.views.expandFriendList'),
	url(r'^expandGroupList/$', 'status.views.expandGroupList'),
	url(r'^click/$', 'status.views.showGroupStatus'),
	url(r'^headup/$', 'status.views.headup'),
	url(r'^filterCheck$', 'status.views.filterCheck'),
)