#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: format.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2022, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""
from flask import jsonify


class MultiObj(object):
    def __init__(self, obj, *args):
        self.obj = obj
        self.args = args

    def to_json(self):
        ret = {}
        items = []
        if isinstance(self.obj, list):
            items = self.obj

        if hasattr(self.obj, 'items'):
            items = self.obj.items

        for one in items:
            inner = {}
            for arg in self.args:
                inner[arg] = str(getattr(one, '{0}'.format(arg)))

            if inner:
                ret[one.id] = inner

        return ret


class OneObj(object):
    def __init__(self, obj, *args):
        self.obj = obj
        self.args = args

    def to_json(self):
        ret = {}
        for arg in self.args:
            ret[arg] = str(getattr(self.obj, '{0}'.format(arg)))

        return jsonify(**ret)


class FixOutput(object):
    @classmethod
    def to_json(cls):
        return jsonify(message='success')

    @classmethod
    def failed_json(cls, msg):
        return jsonify(message='fail', msg=msg)
