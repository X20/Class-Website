from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demo.views.home', name='home'),
    # url(r'^demo/', include('demo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'userlogin.views.index'),
	url(r'^login/$', 'userlogin.views.userLogin'),
	url(r'^logout/$', 'userlogin.views.userLogout'),
	url(r'^toRegister/$', 'userlogin.views.toRegister'),
	url(r'^register/$', 'userlogin.views.register'),
	url(r'^homepage/', include('home.urls')),
	url(r'^file/', include('file.urls')),
	url(r'^messege/', include('messege.urls')),
	url(r'^status/', include('status.urls')),
)