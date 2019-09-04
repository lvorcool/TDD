# coding:utf-8
# @Time  : 2019-09-04 18:21
# @Author: Xiawang
# Description:
from scripts.args_6 import Args6


class Test_args6:

    def test_args(self):
        schema_text = 'l:bool p:int d:str'
        command_text = 'l true p 8080 d /usr/local'
        assert Args6(schema_text, command_text).get_value('l') == True
        assert Args6(schema_text, command_text).get_value('p') == 8080
        assert Args6(schema_text, command_text).get_value('d') == '/usr/local'
