# -*- coding: utf-8 -*-
from os.path import join, dirname
from setuptools import setup, find_packages


version = __import__('django_info').__version__


LONG_DESCRIPTION = """
django_info
===================

Django application to display useful information about a Django project.

    $ git clone git://github.com/marcelor/django_info.git
"""


def long_description():
    try:
        return open(join(dirname(__file__), 'README.md')).read()
    except IOError:
        return LONG_DESCRIPTION


setup(name='django-info',
      version=version,
      author='marcelor',
      author_email='marcelor@gmail.com',
      description='Django application to display useful information about a Django project.',
      download_url='https://github.com/marcelor/django_info/zipball/master/',
      license='BSD',
      keywords='django, runtime information, installed apps',
      url='https://github.com/marcelor/django_info',
      packages=find_packages(),
      include_package_data=True,
      long_description=long_description(),
      install_requires=['django>=1.0', ],
      classifiers=['Framework :: Django',
                   'Development Status :: 3 - Alpha',
                   'Topic :: Internet',
                   'License :: OSI Approved :: BSD License',
                   'Intended Audience :: Developers',
                   'Environment :: Web Environment',
                   'Programming Language :: Python :: 2.5',
                   'Programming Language :: Python :: 2.6',
                   'Programming Language :: Python :: 2.7'])
