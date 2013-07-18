from django.conf.urls import patterns, include, url

urlpatterns=patterns(''
		url(r'^$', 'file.views.showPage'),
		url(r'^clickGroup/$', 'file.views.clickGroup'),
		url(r'^upload/$', 'file.views.upload'),
		url(r'^download/$', 'file.views.download'),
	)