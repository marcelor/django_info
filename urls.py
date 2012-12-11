from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^info/$', 'djangoinfo.views.info', name='info'),
)
