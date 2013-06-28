try:
    from django.conf.urls.defaults import *
except ImportError:
    from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^info/$', 'django_info.views.info', name='info'),
)
