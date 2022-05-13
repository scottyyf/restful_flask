#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: format.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2022, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""
import json

from flask import jsonify, make_response


class MultiObj(object):
    def __init__(self, obj, *args, status_code=200):
        self.obj = obj
        self.args = args
        self.status_code = status_code

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

        rsp = make_response(json.dumps(ret), self.status_code)
        rsp.headers.update({'Content-Type': 'application/json'})

        return rsp


class OneObj(object):
    def __init__(self, obj, *args, status_code=200):
        self.obj = obj
        self.args = args
        self.status_code = status_code

    def to_json(self):
        ret = {}
        for arg in self.args:
            ret[arg] = str(getattr(self.obj, '{0}'.format(arg)))

        rsp = make_response(json.dumps(ret), self.status_code)
        rsp.headers.update({'Content-Type': 'application/json'})
        return rsp


class FixOutput(object):
    @classmethod
    def to_json(cls, status_code=200):
        rsp = make_response(json.dumps({'message': 'success'}), status_code)
        rsp.headers.update({'Content-Type': 'application/json'})
        return rsp

    @classmethod
    def failed_json(cls, msg, status_code=200):
        rsp = make_response(json.dumps(
            {'message': 'fail', 'msg': msg}), status_code)
        rsp.headers.update({'Content-Type': 'application/json'})
        return rsp
