#!/usr/bin/env python
# encoding:utf-8
# me@archie.cc


import yaml
import os



code = yaml.load(open('../common/response_code.yaml'))

# if not os.path.isfile('../common/response_code.py'):
f = open('../common/response_code.py', 'w')
f.write('pass')
