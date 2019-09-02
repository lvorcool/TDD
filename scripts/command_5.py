# coding:utf-8
# @Time  : 2019-09-02 21:30
# @Author: Xiawang
# Description:


class Command:
    def __init__(self, command_text):
        self.command_text = command_text

    def command_parse(self):
        command_list = self.command_text.split(' ')
        command_result = {}
        for index, c in enumerate(command_list):
            if c[0] == '-':
                command_result[c] = None
                continue
            command_result[command_list[index - 1]] = c
        return command_result

    def get(self, flag):
        command_result = self.command_parse()
        return command_result.get('-' + flag, None)
