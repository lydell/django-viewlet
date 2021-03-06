# coding=utf-8
from __future__ import unicode_literals
from django.conf import settings as django_settings


class ViewletSettings(dict):

    def __init__(self, **conf):
        super(ViewletSettings, self).__init__(conf)

        # Override defaults with django settings
        for key in conf:
            setattr(self, key, getattr(django_settings, key, conf[key]))

    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__


settings = ViewletSettings(**{
    'VIEWLET_DEFAULT_CACHE_ALIAS': 'viewlet',
    'VIEWLET_TEMPLATE_ENGINE': 'django',
    'VIEWLET_INFINITE_CACHE_TIMEOUT': 31104000,  # 60*60*24*30*12, about a year
    'VIEWLET_JINJA2_ENVIRONMENT': 'viewlet.loaders.jinja2_loader.create_env'
})
