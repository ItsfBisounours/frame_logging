=============================
Frame Logging
=============================

.. image:: https://badge.fury.io/py/frame_logging.svg
    :target: https://badge.fury.io/py/frame_logging

.. image:: https://travis-ci.org/ItsfBisounours/frame_logging.svg?branch=master
    :target: https://travis-ci.org/ItsfBisounours/frame_logging

.. image:: https://codecov.io/gh/ItsfBisounours/frame_logging/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/ItsfBisounours/frame_logging

Your project description goes here

Documentation
-------------

The full documentation is at https://frame_logging.readthedocs.io.

Quickstart
----------

Install Frame Logging::

    pip install frame_logging

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'frame_logging.apps.FrameLoggingConfig',
        ...
    )

Add Frame Logging's URL patterns:

.. code-block:: python

    from frame_logging import urls as frame_logging_urls


    urlpatterns = [
        ...
        url(r'^', include(frame_logging_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
