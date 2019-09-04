# coding:utf-8
# @Time  : 2019-09-02 21:01
# @Author: Xiawang

import pytest
from scripts.schema_4 import Schema


class Test_test_schema_4:
    def test_schema(self):
        schema_text = 'l:bool p:int d:str'
        command_text ='l true p 8080 d /usr/local'
        assert Schema(schema_text).get('l','true') == True
        assert Schema(schema_text).get('p', '8080') == 8080
        assert Schema(schema_text).get('d','/usr/local') == '/usr/local'
