# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from testfixtures import LogCapture

import frame_logging.log as log


class Order(object):
    def __init__(self):
        self.customer = {'id': 1}


class FrameLoggingTest(TestCase):

    def test_default_info(self):
        with LogCapture() as l:
            log.info('Renewed contract %s', 'test')
            l.check(('tests.test_frame_logging', 'INFO', 'Renewed contract test'))

    def test_info_with_task(self):
        class Task(object):
            def __init__(self):
                self.id = 1

        with LogCapture() as l:
            log.info('Renewed contract %s', 'test', task=Task())
            l.check(('tests.test_frame_logging', 'INFO', 'Renewed contract test - task_id=1'))

    def test_default_debug(self):
        with LogCapture() as l:
            log.debug('Renewed contract %s', 'test')
            l.check(('tests.test_frame_logging', 'DEBUG', 'Renewed contract test'))

    def test_default_critical(self):
        with LogCapture() as l:
            log.critical('Renewed contract %s', 'test')
            l.check(('tests.test_frame_logging', 'CRITICAL', 'Renewed contract test'))

    def test_default_warning(self):
        with LogCapture() as l:
            log.warning('Renewed contract %s', 'test')
            l.check(('tests.test_frame_logging', 'WARNING', 'Renewed contract test'))

    def test_default_error(self):
        with LogCapture() as l:
            log.error('Renewed contract %s', 'test')
            l.check(('tests.test_frame_logging', 'ERROR', 'Renewed contract test'))

    def test_default_exception(self):
        with LogCapture() as l:
            try:
                raise ValueError("This is a test")
            except ValueError:
                log.exception('Renewed contract %s', 'test')
            l.check(('tests.test_frame_logging', 'ERROR', 'Renewed contract test'))

    def test_custom_format(self):
        class TestObj(object):
            def __init__(self):
                self.t_attr = 't_val'
            def __str__(self):
                return self.t_attr
        with LogCapture() as l:
            test_obj = TestObj()
            test_obj.tn_attr = 'tn_val'
            log.error('Renewed contract %s', 'test', obj=test_obj)
            l.check(('tests.test_frame_logging',
                     'ERROR', 'Renewed contract test - Impacted object is TestObj(t_val):'
                              ' tn_attr=tn_val, t_attr=t_val'))

    def test_transform(self):
        order = Order()
        with LogCapture() as l:
            #import pdb; pdb.set_trace()
            log.info('Renewed contract %s', 'test', order=order)
            l.check(('tests.test_frame_logging', 'INFO', 'Renewed contract test - customer_id=1'))

if __name__ == '__main__':
    unittest.main()
