# coding:utf-8
# @Time  : 2019-08-23 12:29
# @Author: Xiawang
# Description:
from scripts.command_parse import CommandParse
from scripts.schema_parse import SchemaParse


class ArgsParse:

    def __init__(self, schema_text, command_text):
        self.schema = SchemaParse(schema_text)
        self.command = CommandParse(command_text)


    def get_value(self,name):
        return self.schema.get_value(name,self.command.get_value(name))
