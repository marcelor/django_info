# -*- coding: utf-8 -*-
import os
import sys
from django.contrib.auth.decorators import login_required
from django import get_version as get_django_version
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.conf import settings


def get_platform():
    return ' '.join(os.uname())


def get_python_version():
    return sys.version


def get_database_engine():
    return settings.DATABASES['default']['ENGINE'].split('.')[-1]


@login_required(login_url="/admin/")
def info(request):

    context = {
        'django_version':  get_django_version(),
        'database_engine': get_database_engine(),
        'python_version': get_python_version(),
        'platform': get_platform(),
    }

    return render_to_response('info.html', context,
                          context_instance=RequestContext(request))
