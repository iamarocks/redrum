#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from util import redis


class DictionaryModel(object):
    """
    CachedDataObjects are for centralizing and organizing entries
    to and from Redis or any cache. Currently it supports objects which
    have simple properties or properties which can be either lists or dictionaries
    This actually gets you pretty far
    """

    _cache_db = None

    def __init__(self):
        self._object_key = None
        self._exp_seconds = None

    def get_cache_key(self, *args, **kwargs):
        raise NotImplementedError

    def serialize(self):
        """
        This does not yet account for any properties that may be objects themselves
        """
        srzl = dict()
        for name in dir(self):
            value = getattr(self, name)
            if (not name.startswith('_') or name == '__name__') and not callable(value):
                if name == '__name__':
                    srzl['type'] = value
                else:
                    if hasattr(value, '__iter__'):
                        if hasattr(value, '__dict__'):
                            srzl[name] = dict()
                            for k, v in value:
                                srzl[name][k] = v
                        else:
                            srzl[name] = list()
                            for i in value:
                                srzl[name].append(i)
                    else:
                        srzl[name] = value
        return json.dumps(srzl)

    def from_dict(self, data):
        """ Deserialize from a dictionary to object attributes """
        for k, v in data.items():
            setattr(self, k, v)
        return self

    def read(self, object_key):
        """ Read data from Redis
        :param object_key:
        :return: dictionary of attributes
        """
        read_key = self.get_cache_key(object_key)
        with redis.read_connection(self._cache_db) as conn:
            raw_data = conn.get(read_key)
            data_dict = json.loads(raw_data)
            return self.from_dict(data_dict)

    def write(self, exp_seconds=None):
        """
        Write data to redis
        :return: True
        """
        object_key = getattr(self, self._object_key)
        write_key = self.get_cache_key(object_key)
        if exp_seconds is not None:
            expiration_seconds = exp_seconds
        elif self._exp_seconds is not None:
            expiration_seconds = self._exp_seconds
        else:
            expiration_seconds = None

        with redis.write_connection(self._cache_db) as conn:
            if expiration_seconds is None:
                conn.set(write_key, self.serialize())
            else:
                conn.setex(write_key, self.serialize(), expiration_seconds)
            return True

    def delete(self):
        """
        Delete associated record
        :return: True on success
        """
        object_key = getattr(self, self._object_key)
        with redis.write_connection(self._cache_db) as conn:
            conn.delete(object_key)
