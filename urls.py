from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^info/$', 'djangoinfo.views.info', name='info'),
)
