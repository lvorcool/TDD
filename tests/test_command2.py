# coding:utf-8
# @Time  : 2019-08-23 16:03
# @Author: Xiawang

import pytest
from scripts.command_parse import CommandParse


class Test_test_command2:
    @pytest.mark.parametrize('commandline', [('-l true -d /usr/local -p 8080')])
    def test_has_value(self, commandline):
        command_parse = CommandParse(commandline)
        assert command_parse.get_value('l') == 'true'
        assert command_parse.get_value('d') == '/usr/local'
        assert command_parse.get_value('p') == '8080'

    @pytest.mark.parametrize('commandline', [('-l -d /usr/local -p 8080')])
    def test_has_no_value(self, commandline):
        command_parse = CommandParse(commandline)
        assert command_parse.get_value('l') == None
        assert command_parse.get_value('d') == '/usr/local'
        assert command_parse.get_value('p') == '8080'
