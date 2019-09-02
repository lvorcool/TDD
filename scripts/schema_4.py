# coding:utf-8
# @Time  : 2019-09-02 21:03
# @Author: Xiawang
# Description:

class Schema:
    def schema_parse(self,schema_text):
        schema_result = {}
        for s in schema_text.split(' '):
            flag_name, flag_value = s.split(':')
            schema_result[flag_name] = flag_value
        return schema_result

    def get(self, flag):
        if flag == 'l':
            return 'bool'
        elif flag == 'p':
            return 'int'
        elif flag == 'd':
            return 'str'
