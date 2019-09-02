# coding:utf-8
# @Time  : 2019-09-02 21:01
# @Author: Xiawang

import pytest
from scripts.schema_4 import Schema


class Test_test_schema_4:
    def test_schema(self):
        schema_text = 'l:bool p:int d:str'
        assert Schema().get('l') == 'bool'
        assert Schema().get('p') == 'int'
        assert Schema().get('d') == 'str'
