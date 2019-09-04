# coding:utf-8
# @Time  : 2019-09-04 18:25
# @Author: Xiawang
# Description:
from scripts.schema_4 import Schema
from scripts.command_5 import Command


class Args6:

    def __init__(self, schema_text, command_text):
        self.schema = Schema(schema_text)
        self.command = Command(command_text)

    def get_value(self, flag):
        return self.schema.get(self.command.get(flag))
