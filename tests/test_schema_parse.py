# coding:utf-8
# @Time  : 2019-08-23 13:25
# @Author: Xiawang

import pytest
from scripts.schema_parse import SchemaParse


class Test_test_schema_parse:
    @pytest.mark.parametrize("schema_text", [('l:bool,p:int,d:str')])
    def test_schema_parse(self, schema_text):
        schema = SchemaParse(schema_text)
        assert schema.get_value('l', 'true') == True
        assert schema.get_value('l', 'false') == False
        assert schema.get_value('l', None) == False
        assert schema.get_value('p', '8080') == 8080
        assert schema.get_value('d', '/usr/local') == '/usr/local'
