# coding:utf-8
# @Time  : 2019-09-02 21:30
# @Author: Xiawang
# Description:


class Command:
    def __init__(self,command_text):
        self.command_text = command_text

    def get(self,flag):
        if 'l' in self.command_text:
            return True
