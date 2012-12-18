# -*- coding: utf-8 -*-
import os
import sys
from django.contrib.auth.decorators import login_required
from django import get_version as get_django_version
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.conf import settings
from django_info import __version__


def django_info_version():
    return __version__


def get_platform():
    return ' '.join(os.uname())


def get_python_version():
    return sys.version


def get_database_engine():
    return settings.DATABASES['default']['ENGINE'].split('.')[-1]


def get_installed_apps():
    return settings.INSTALLED_APPS


def get_debug_mode():
    return settings.DEBUG


def get_template_debug_mode():
    return settings.TEMPLATE_DEBUG


def is_dev_server(request):
    """
    http://stackoverflow.com/a/1291858/1503
    """
    server_software = request.META.get('SERVER_SOFTWARE', None)
    return server_software is not None and ('WSGIServer' in server_software or 'Python' in server_software)


def get_path(request):
    path = request.META.get('PATH', None)
    if path:
        return [p for p in path.split(":")]
    return None


@login_required(login_url="/admin/")
def info(request):

    context = {
        'django_info_version': django_info_version(),
        'django_version':  get_django_version(),
        'database_engine': get_database_engine(),
        'python_version': get_python_version(),
        'platform': get_platform(),
        # settings
        'settings_debug_mode': get_debug_mode(),
        'settings_template_debug_mode': get_template_debug_mode(),
        'settings_installed_apps': get_installed_apps(),
        'is_dev_server': is_dev_server(request),
        'paths': get_path(request),
    }

    return render_to_response('django_info/info.html', context,
                          context_instance=RequestContext(request))
