from django.conf.urls import patterns, include, url
#from mysocialnetwork.views import allusers
from django.contrib import admin
from my_social_network import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url('^users/$', views.alluser),
    url('^(?P<username>\w+)/followers/$', views.allfollowers),
    url('^(?P<username>\w+)/following/$', views.allfollowing),
    
    
)


