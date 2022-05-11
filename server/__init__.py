#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: __init__.py.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2022, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api

# from .routes import add_route
from .config.config import ProductionConfig, DevelopConfig


db = SQLAlchemy()
migrate = Migrate()


def create_app(test_config=True):

    app = Flask(__name__)
    if test_config:
        # to load test config
        app.config.from_object(DevelopConfig)
    else:
        # to load production config
        app.config.from_object(ProductionConfig)

    from .models.works import Plan
    from .models.users import User

    jwt = JWTManager(app)

    @jwt.user_identity_loader
    def user_identity_lookup(user):
        return user.id

    @jwt.user_lookup_loader
    def user_lookup_callback(_, data):
        identity = data['sub']
        return User.query.filter_by(id=identity).one_or_none()

    @jwt.additional_claims_loader
    def add_claims_to_access_token(identity):
        return {
            'attitude': 'support people in Russia'
            }

    db.init_app(app)
    migrate.init_app(app, db)
    api = Api(app, catch_all_404s=True)

    from server.views.plan import DayPlans
    from server.views.add import Add
    from server.views.delete import Delete
    from server.views.modify import Modify
    from server.views.auth import Auth, Login
    api.add_resource(Add, '/add')
    api.add_resource(DayPlans, '/plan')
    api.add_resource(Delete, '/delete')
    api.add_resource(Modify, '/modify')
    api.add_resource(Auth, '/auth')
    api.add_resource(Login, '/login')

    return app
