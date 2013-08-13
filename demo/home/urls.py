from django.conf.urls import patterns, include, url

urlpatterns=patterns('',
		url(r'^$', 'home.views.home'),
		url(r'^allGroup/$', 'home.views.allGroup'),
	)