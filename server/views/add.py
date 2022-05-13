#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: add.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2022, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""
from flask import Blueprint
from flask_jwt_extended import jwt_required
from flask_restful import Resource, reqparse, Api
from datetime import datetime

from server.format.format import FixOutput
from server.models.works import Plan

"""
'add_at', 'start_at', 'end_at', 'name', \
               'description', 'day'
"""


def dt(datetime_str):
    return datetime.fromisoformat(datetime_str)


plan_parser = reqparse.RequestParser()
plan_parser.add_argument('end_at', type=dt, help='', required=True,
                         location=['form'])
plan_parser.add_argument('name', type=str, help='', required=True,
                         location=['form'])
plan_parser.add_argument('description', type=str, help='', required=True,
                         location=['form'])


class Add(Resource):
    weekday_map = {
        1: 'monday',
        2: 'tuesday',
        3: 'wednesday',
        4: 'thursday',
        5: 'friday',
        6: 'saturday',
        7: 'sunday'
        }

    @jwt_required()
    def post(self):
        args = plan_parser.parse_args()
        day = self.weekday_map.get(datetime.now().isoweekday(), 'monday')

        if Plan.query.filter(Plan.name == args.name).all():
            return FixOutput.failed_json('name {0} already exist'.format(
                args.name))

        Plan.create(end_at=args.end_at, name=args.name,
                    description=args.description,
                    day=day)
        return FixOutput.to_json()


add_bp = Blueprint('add', __name__, url_prefix='/add')
add_api = Api(add_bp,catch_all_404s=True)
