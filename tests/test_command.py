# coding:utf-8
# @Time  : 2019-08-16 17:05
# @Author: Xiawang

import pytest
from scripts.command import command


class Test_command:
    def test_command_format(self, ):
        command_input = '-l -p 8080 -d /usr/log'
        assert command(command_input).command_parse() == {'-l': None, '-p': '8080', '-d': '/usr/log'}

    def test_command_len(self):
        command_input = '-l -p 8080 -d /usr/log'
        assert command(command_input).command_len() == 3


