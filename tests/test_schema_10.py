# coding:utf-8
# @Time  : 2019-09-04 19:48
# @Author: Xiawang

import pytest
from scripts.schema10 import Schema10


class Test_test_schema_10:
    def test_schema10(self, ):
        schema_text = 'l:bool p:int d:str'
        assert Schema10(schema_text).get_value('l', 'true') == True
        assert Schema10(schema_text).get_value('p', '8080') == 8080
        assert Schema10(schema_text).get_value('d', '/usr/local') == '/usr/local'
