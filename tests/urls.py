# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from frame_logging.urls import urlpatterns as frame_logging_urls

urlpatterns = [
    url(r'^', include(frame_logging_urls, namespace='frame_logging')),
]
