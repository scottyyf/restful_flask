#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: modify.py
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


def dt(datetime_str):
    return datetime.fromisoformat(datetime_str)


"""
'add_at', 'start_at', 'end_at', 'name', \
               'description', 'day'
"""

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, help='', location=['form', 'args'],
                    required=True)
parser.add_argument('end_at', type=dt, help='', location=['form', 'args'])
parser.add_argument('description', type=str, help='', location=['form', 'args'])


class Modify(Resource):
    @jwt_required()
    def put(self):
        args = parser.parse_args()
        plan = Plan.query.filter_by(name=args.name).first()
        if plan:
            if args.end_at:
                plan.end_at = args.end_at

            if args.description:
                plan.description = args.description

            plan.save()

        return FixOutput.to_json()


mod_bp = Blueprint('modify', __name__, url_prefix='/modify')
mode_api = Api(mod_bp,catch_all_404s=True)
