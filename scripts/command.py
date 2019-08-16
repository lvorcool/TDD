# coding:utf-8
# @Time  : 2019-08-16 17:07
# @Author: Xiawang
# Description:


class command:

    def __init__(self, command_input):
        self.command_input = command_input

    def command_parse(self):
        command_list = self.command_input.split(' ')
        command_format = {}
        for index, command in enumerate(command_list):
            if command[:1] == '-':
                command_format[command] = None
                continue
            command_format[command_list[index - 1]] = command
        return command_format

    def command_len(self):
        return len(self.command_parse())
