# coding:utf-8
# @Time  : 2019-09-04 20:11
# @Author: Xiawang
# Description:
from scripts.command10 import Command10
from scripts.schema10 import Schema10


class Args10:

    def __init__(self, schema_text, command_text):
        self.schema = Schema10(schema_text)
        self.command = Command10(command_text)

    def get_value(self, flag):
        return self.schema.get_value(flag, self.command.get_value('-' + flag))
