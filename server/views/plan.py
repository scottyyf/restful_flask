#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: plan.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2022, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""

from flask_restful import Resource, reqparse, Api
from server.models.works import Plan
from flask import request, Blueprint
from flask_jwt_extended import jwt_required
from server.format.format import MultiObj

dayInWeek_parser = reqparse.RequestParser()
dayInWeek_parser.add_argument('day', dest='day', required=True,
                              location=['args', 'form'],
                              help="day of the weekend, must be one of"
                                   " 'monday', 'tuesday', 'wednesday', "
                                   "'thursday', 'friday', 'saturday','sunday'",
                              choices=['monday', 'tuesday', 'wednesday',
                                       'thursday', 'friday', 'saturday',
                                       'sunday'])

dayInWeek_parser.add_argument('page', type=int,
                              location=['args', 'form'], default=1)
dayInWeek_parser.add_argument('per_page', type=int,
                              location=['args', 'form'], default=5)


class DayPlans(Resource):
    @jwt_required()
    def get(self):
        """
        day_in_week is monday tuesday ...
        """
        if 'day' not in request.args:
            if 'page' not in request.args:
                plan = Plan.query.order_by(Plan.start_at).all()
            else:
                plan = Plan.query.order_by(
                    Plan.start_at).paginate(int(request.args['page']),
                                            int(request.args['per_page']),
                                            error_out=False)
        else:
            args = dayInWeek_parser.parse_args()
            plan = Plan.query.filter_by(day=args.day).order_by(
                Plan.start_at).paginate(args.page, args.per_page,
                                        error_out=False)
        ret = MultiObj(plan, *Plan.column_args())
        return ret.to_json()


plan_bp = Blueprint('plan', __name__, url_prefix='/plan')
plan_api = Api(plan_bp,catch_all_404s=True)
