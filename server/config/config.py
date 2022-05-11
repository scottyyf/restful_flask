#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: __init__.py.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2022, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""
from datetime import timedelta


class BasicConfig(object):
    TESTING = True
    SECRET_KEY = 'flask-worker-plan-restful-2022'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "!1hh23siwoo*7{-1GAB."

    # flask restful error handler for requestparser
    BUNDLE_ERRORS = True

    # flask jwt extend
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=1)


class DevelopConfig(BasicConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = \
        'mysql://root:my-secret-pw@192.168.4.91:3306/plan-work-dev'


class ProductionConfig(BasicConfig):
    import secrets
    TESTING = False
    SQLALCHEMY_DATABASE_URI =\
        'mysql://root:my-secret-pw@192.168.4.91:3306/plan-work-pro'
    SECRET_KEY = secrets.token_hex()
