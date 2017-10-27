# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from collections import OrderedDict
from frame_logging.formatter import FrameFormatter


class FrameFormatterExample(FrameFormatter):

    # format methods

    @classmethod
    def get_format_behaviour(cls):
        return OrderedDict([
            ('task_id', cls.format_task_id),
            ('obj', cls.default_object_serialisation),
            ('customer_id', cls.format_customer_id),
        ])

    @classmethod
    def format_customer_id(cls, customer_id):
        return "customer_id={}".format(customer_id)

    @classmethod
    def _format_obj_attr(cls, attr_dict):
        instance_attributes_str = ''
        for attr, val in attr_dict:
            if instance_attributes_str:
                instance_attributes_str += ', '
            instance_attributes_str += "{field_name}={value}".format(
                field_name=attr,
                value=val,
            )
        return instance_attributes_str
    
    @classmethod
    def default_object_serialisation(cls, obj):
        if type(obj) == dict:
            instance_attributes_str = cls._format_obj_attr(obj.iteritems())
        else:
            # assume type(obj) is object
            instance_attributes_str = cls._format_obj_attr(obj.__dict__.items())
        return "Impacted object is {class_name}({instance_name}): {instance_attributes}".format(
            class_name=obj.__class__.__name__,
            instance_name=obj,
            instance_attributes=instance_attributes_str,
        )
    
    @classmethod
    def format_task_id(cls, task_id):
        return "task_id={}".format(task_id)

    # then if you need to, you can add new method to transform extra kwargs
    # transform methods

    @classmethod
    def get_transform_kwargs_methods(cls):
        return   {
            'task': cls.transform_task,
            'order': cls.transform_order,
        }

    @classmethod
    def transform_task(cls, task, **kwargs):
        kwargs['task_id'] = task.__dict__.get('id', '')
        return kwargs

    @classmethod
    def transform_order(cls, order, **kwargs):
        kwargs['customer_id'] = order.customer['id']
        return kwargs
