# coding:utf-8
# @Time  : 2019-09-02 21:03
# @Author: Xiawang
# Description:

class Schema:
    def __init__(self, schema_text):
        self.schema_text = schema_text

    def schema_parse(self):
        schema_result = {}
        for s in self.schema_text.split(' '):
            flag_name, flag_value = s.split(':')
            schema_result[flag_name] = flag_value
        return schema_result

    def get(self, flag_name, flag_value):
        flag_type = self.schema_parse().get(flag_name)
        if flag_type == 'bool':
            return 'true' == flag_value or not flag_value
        elif flag_type == 'int':
            return int(flag_value)
        else:
            return flag_value
