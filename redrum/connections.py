#!/usr/bin/env python
# -*- coding: utf-8 -*-

import contextlib
import dbsettings

import redis


@contextlib.contextmanager
def connection(db_name):
    dbnum = dbsettings.dbnames.get(db_name)
    yield redis.StrictRedis(host=dbsettings.db['host'], port=dbsettings.db['port'], db=dbnum)
