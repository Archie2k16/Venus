#!/usr/bin/env python
# encoding:utf-8
# me@archie.cc
'''
This is the common dot_dict class
which is used for easier dict access
>>> a=dot_dict({'hello':'world'})
>>> a.hello
World
'''


class dot_dict(object):
    def __init__(self, obj):
        self._map = obj

    def __setattr__(self, key, value):
        if key.startswith('_'):
            super(dot_dict, self).__setattr__(key, value)
        else:
            self._map[key] = value

    def __getattr__(self, key):
        return self._map[key]

    def __repr__(self):
        return repr(self._map)

    def __str__(self):
        return self.__repr__()
