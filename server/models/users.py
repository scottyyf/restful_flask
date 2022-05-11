#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: users.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2022, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""
from server import db
from sqlalchemy import Column, String, Text, DateTime, TIMESTAMP, text, Integer
from werkzeug.security import check_password_hash, generate_password_hash


class UserMixin(object):

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        instance.save()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class User(db.Model, UserMixin):
    __tablename__ = 'tbs_user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    create_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))
    name = Column(String(100), nullable=False, unique=True)
    password = Column(String(200), nullable=False)

    def __repr__(self):
        return '{0}'.format(self.name)
