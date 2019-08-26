# coding:utf-8
# @Time  : 2019-08-23 12:19
# @Author: Xiawang

import pytest
from scripts.args_parse import ArgsParse


class Test_test_args_parse:
    @pytest.mark.parametrize('schema_text,command_text', [('l:bool,p:int,d:str', '-l true -p 8080 -d /usr/local')])
    def test_args(self, schema_text, command_text):
        arg_parse = ArgsParse(schema_text, command_text)
        assert arg_parse.get_value('l') == True
        assert arg_parse.get_value('p') == 8080
        assert arg_parse.get_value('d') == '/usr/local'
        assert arg_parse.get_value('s') == '没有该参数, 请重新输入'
