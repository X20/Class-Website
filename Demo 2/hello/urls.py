from django.conf.urls import patterns, include, url
#import login.urls as login_urls
#from login.views import index

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hello.views.home', name='home'),
    # url(r'^hello/', include('hello.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^$', 'userlogin.views.index'),
    url(r'^login/$', 'userlogin.views.userlogin'),
    url(r'^logout/$', 'userlogin.views.userlogout'),
    url(r'^home/$', 'userlogin.views.home'),
    # url(r'^user/', include(login_urls)),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^static/$', 'static'),
)