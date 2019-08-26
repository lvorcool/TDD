# coding:utf-8
# @Time  : 2019-08-23 16:07
# @Author: Xiawang
# Description:


class CommandParse:

    def __init__(self, command_line):
        self.command_line = command_line

    def command_parse(self):
        command_dict = {}
        command_iter = iter(self.command_line.split(' '))
        while True:
            try:
                flag_name = next(command_iter)
                flag_value = next(command_iter)
                if flag_value[0] != '-':
                    command_dict.setdefault(flag_name, flag_value)
                else:
                    command_dict.setdefault(flag_name)
                    command_dict.setdefault(flag_value, next(command_iter))
            except StopIteration:
                break
        return command_dict

    def get_value(self, flag):
        command_dict = self.command_parse()
        return command_dict.get('-' + flag, None)

