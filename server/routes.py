#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: routes.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2022, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""
from server.views.plan import DayPlans, plan_bp, plan_api
from server.views.add import Add, add_bp, add_api
from server.views.delete import Delete, del_bp, del_api
from server.views.modify import Modify, mod_bp, mode_api
from server.views.auth import (Auth, Login, auth_bp, auth_api,
                               login_api, login_bp)


def add_route(app):
    app.register_blueprint(add_bp)
    add_api.add_resource(Add, '/add')

    app.register_blueprint(plan_bp)
    plan_api.add_resource(DayPlans, '/plan')

    app.register_blueprint(del_bp)
    del_api.add_resource(Delete, '/delete')

    app.register_blueprint(mod_bp)
    mode_api.add_resource(Modify, '/modify')

    app.register_blueprint(auth_bp)
    auth_api.add_resource(Auth, '/auth')

    app.register_blueprint(login_bp)
    login_api.add_resource(Login, '/login')
