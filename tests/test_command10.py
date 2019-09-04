# coding:utf-8
# @Time  : 2019-09-04 19:58
# @Author: Xiawang
# Description:


import pytest
from scripts.command10 import Command10

class Test_test_command10:
    def test_command10(self, ):
        command_text = '-l true -p 8080 -d /usr/local'
        assert Command10(command_text).get_value('l') == 'true'

