#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: works.py
Author: Scott Yang(Scott)
Email: yangyingfa@skybility.com
Copyright: Copyright (c) 2022, Skybility Software Co.,Ltd. All rights reserved.
Description:
"""
from server import db
# from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, Text, text, String


class CRUDMixin(object):
    def __repr__(self):
        return "{0}".format(self.__class__.__name__)

    def save(self):
        """Plan's instance can call save to add flag to db"""
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def create(cls, *args, **kwarg):
        instance = cls(*args, **kwarg)
        instance.save()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Plan(db.Model, CRUDMixin):
    __tablename__ = 'tlb_work_plan'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    add_at = Column(DateTime, nullable=False,
                    server_default=text('CURRENT_TIMESTAMP'))
    start_at = Column(DateTime, nullable=False,
                      server_default=text('CURRENT_TIMESTAMP'))
    end_at = Column(DateTime, nullable=False)
    name = Column(String(300), nullable=True, unique=True)
    description = Column(Text, nullable=True)
    day = Column(String(20), nullable=True)

    def __repr__(self):
        return '{0}'.format(self.name)

    @classmethod
    def column_args(cls):
        return 'id', 'add_at', 'start_at', 'end_at', 'name', \
               'description', 'day'
