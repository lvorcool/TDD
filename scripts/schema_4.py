# coding:utf-8
# @Time  : 2019-09-02 21:03
# @Author: Xiawang
# Description:

class Schema:

    def get(self, flag):
        if flag == 'l':
            return 'bool'
        elif flag == 'p':
            return 'int'
        elif flag == 'd':
            return 'str'
