# coding:utf-8
# @Time  : 2019-09-04 19:50
# @Author: Xiawang
# Description:

class Schema10:

    def __init__(self, schema_text):
        self.schema_text = schema_text

    def schema_parse(self):
        schema_result = {}
        for s in self.schema_text.split(' '):
            flag_name, flag_type = s.split(':')
            schema_result[flag_name] = flag_type
        return schema_result

    def get_value(self, flag, str_value):
        flag_type = self.schema_parse().get(flag)
        if flag_type == 'bool':
            return 'true' == str_value or not str_value
        elif flag_type == 'int':
            return int(str_value)
        else:
            return str_value
