# coding:utf-8
# @Time  : 2019-09-04 20:09
# @Author: Xiawang

import pytest
from scripts.args10 import Args10


class Test_test_args10:
    def test_args(self, ):
        schema_text = 'l:bool p:int d:str'
        command_text = '-l true -p 8080 -d /usr/local'
        Args10(schema_text, command_text).get_value('l') == True
        Args10(schema_text, command_text).get_value('p') == 8080
        Args10(schema_text, command_text).get_value('d') == '/usr/local'
