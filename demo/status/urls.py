from django.conf.urls import patterns, include, url

urlpatterns=patterns('',
	url('^$', 'status.views.statusPage'),
	url('^expandFriendList/$', 'status.views.expandFriendList')
	url('^expandGroupList/$', 'status.views.expandGroupList'),
	url(r'^click/$', 'status.views.showGroupStatus'),
	url(r'^headup/$', 'status.views.headup'),
	url(r'^filterCheck$', 'status.views.filterCheck'),
)