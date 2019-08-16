# coding:utf-8
# @Time  : 2019-08-16 18:08
# @Author: Xiawang

import pytest
from scripts.argsParse import argsParse


class Test_test_argsParse:
    def test_arg_type(self, ):
        args = {'-l': False, '-p': '8080', '-d': '/usr/log'}
        schema = {'l': ('bool', False, '该参数 l 的类型是 bool'),
                  'p': ('int', 0, '该参数 p 的类型是 int'),
                  'd': ('str', '', '该参数 d 的类型是 str')}
        assert argsParse(schema, args).assert_flag_type('l') == True

    def test_arg_consistent(self, ):
        args = {'-l': False, '-p': '8080', '-d': '/usr/log'}
        schema = {'l': ('bool', False, '该参数 l 的类型是 bool'),
                  'p': ('int', 0, '该参数 p 的类型是 int'),
                  'd': ('str', '', '该参数 d 的类型是 str')}
        assert argsParse(schema, args).assert_flag_consistent() == True


    def test_arg_value(self, ):
        args = {'-l': False, '-p': '8080', '-d': '/usr/log'}
        schema = {'l': ('bool', False, '该参数 l 的类型是 bool'),
                  'p': ('int', 0, '该参数 p 的类型是 int'),
                  'd': ('str', '', '该参数 d 的类型是 str')}
        assert argsParse(schema, args).get_flag_value('l') == False
