# coding:utf-8
# @Time  : 2019-09-04 20:00
# @Author: Xiawang
# Description:

class Command10:

    def __init__(self, command_text):
        self.command_text = command_text

    def command_parse(self):
        command_result = {}
        command_list = self.command_text.split(' ')
        for index, c in enumerate(command_list):
            if c[0] == '-':
                command_result[c] = None
                continue
            command_result[command_list[index - 1]] = c
        return command_result

    def get_value(self, flag):
        return self.command_parse().get(flag)
