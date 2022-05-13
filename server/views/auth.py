#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: auth.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2022, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""

from flask_restful import Resource, Api
from flask import request, jsonify, Blueprint
from flask_jwt_extended import (jwt_required, create_access_token,
                                create_refresh_token,
                                get_current_user)
from werkzeug.security import generate_password_hash, check_password_hash

from server.format.format import FixOutput, MultiObj
from server.models.users import User


class Auth(Resource):
    @jwt_required()
    def get(self):
        """
        get current jwt token
        """
        user = User.query.all()
        return MultiObj(user, 'id', 'name').to_json()

    @jwt_required()
    def post(self):
        """
        post user and password
        return: refresh token and access token
        """
        name = request.form.get('name', '').strip()
        password = request.form.get('password', '')
        msg = ''
        if not name:
            msg += 'user name is empty.'
        if not password:
            msg += ' password is empty.'

        elif User.query.filter_by(name=name).first():
            msg += 'user {0} is already exist'.format(name)

        if msg:
            return FixOutput.failed_json(msg)

        password = generate_password_hash(password)
        User.create(name=name, password=password)
        return FixOutput.to_json()

    @jwt_required()
    def delete(self):
        """
        delete current user token, include refresh and access token
        """
        name = request.form.get('name', '')
        password = request.form.get('password', '')

        user = User.query.filter_by(name=name).first()
        if user:
            if check_password_hash(user.password, password):
                user.delete()

            else:
                return FixOutput.failed_json('password not match')

        return FixOutput.to_json()


class Login(Resource):
    def post(self):
        name = request.form.get('name', '')
        password = request.form.get('password', '')

        user = User.query.filter_by(name=name).first()
        if user and check_password_hash(user.password, password):
            access_token = create_access_token(identity=user)
            refresh_token = create_refresh_token(identity=user)

        return jsonify(token=access_token, refresh_token=refresh_token)

    @jwt_required(refresh=True)
    def put(self):
        identity = get_current_user()
        access_token = create_access_token(identity=identity, fresh=True)
        return jsonify(token=access_token)


auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
auth_api = Api(auth_bp,catch_all_404s=True)

login_bp = Blueprint('login', __name__, url_prefix='/login')
login_api = Api(login_bp, catch_all_404s=True)
