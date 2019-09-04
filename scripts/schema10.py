# coding:utf-8
# @Time  : 2019-09-04 19:50
# @Author: Xiawang
# Description:

class Schema10:

    def __init__(self, schema_text):
        self.schema_text = schema_text

    def get_value(self,flag):
            if flag == 'l':
                return 'bool'

