#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: del.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2022, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""
from flask import Blueprint
from flask_jwt_extended import jwt_required
from flask_restful import Resource, reqparse, Api
from server.format.format import FixOutput
from server.models.works import Plan

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, help='', location=['form', 'args'])


class Delete(Resource):
    @jwt_required()
    def delete(self):
        args = parser.parse_args()
        plan = Plan.query.filter_by(name=args.name).first()
        if plan:
            plan.delete()

        return FixOutput.to_json(status_code=201)


del_bp = Blueprint('delete', __name__, url_prefix='/delete')
del_api = Api(del_bp,catch_all_404s=True)
