django_info
===========

Django application to display useful information about a Django project. Something like php_info()

Requirements
=========

* Python >= 2.5
* Django >= 1.0


How to install
========

Via pip install:

> pip install django_info

or, manually:


* Add  'django_info' to INSTALLED_APPS

* Add  url(r'^django/', include('django_info.urls')) to the global urls.py

* Visit the url /django/info/