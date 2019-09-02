# coding:utf-8
# @Time  : 2019-09-02 21:24
# @Author: Xiawang

import pytest
from scripts.command_5 import Command

class Test_test_command_5:
    def test_command(self, ):
        command_text = '-l true -p 8080 -d /usr/local'
        assert Command(command_text).get('l') == True


