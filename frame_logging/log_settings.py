# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

from django.conf import settings


FRAME_FORMATTER = getattr(settings, 'FRAME_FORMATTER', None)


if FRAME_FORMATTER is None:
	raise ValueError('Improperly Configured FRAME_FORMATTER')
