# coding:utf-8
# @Time  : 2019-08-16 17:29
# @Author: Xiawang

import pytest
from scripts.schema import schemaParse


class Test_test_schema:
    def test_schema_parse(self, ):
        schema_text = 'l:bool p:int d:str'
        # schema_text = 'l:bool'
        assert schemaParse(schema_text).schema_parse() == {'l': (bool, False, '该参数 l 的类型是 bool'),
                                                           'p': (int, 0, '该参数 p 的类型是 int'),
                                                           'd': (str, '', '该参数 d 的类型是 str')}

    def test_schema_len(self):
        schema_text = 'l:bool p:int d:str'
        assert schemaParse(schema_text).schema_len() == 3
