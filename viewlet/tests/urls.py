# coding=utf-8
from __future__ import unicode_literals
try:
    from django.conf.urls import patterns, include
except ImportError:
    from django.conf.urls.defaults import patterns, include

urlpatterns = patterns(
    '',
    (r'^viewlet/', include('viewlet.urls')),
)
