from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^info/$', 'django_info.views.info', name='info'),
)
