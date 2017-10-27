=====
Usage
=====

To use Frame Logging in a project, add it to your `INSTALLED_APPS`:

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
