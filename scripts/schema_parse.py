# coding:utf-8
# @Time  : 2019-08-23 14:22
# @Author: Xiawang
# Description:

class SchemaParse:
    def __init__(self, schema_text):
        self.schema_text = schema_text

    def schema_parse(self):
        schema_dict = {}
        for schema in self.schema_text.split(','):
            flag_name, flag_type = schema.split(':')
            schema_dict.setdefault(flag_name, flag_type)
        return schema_dict

    def get_value(self, name, str_value):
        flag_type = self.schema_parse().get(name)
        if flag_type == 'bool':
            return 'true' == str_value or not str_value
        elif flag_type == 'int':
            return int(str_value)
        elif flag_type == None:
            return '没有该参数, 请重新输入'
        else:
            return str_value
