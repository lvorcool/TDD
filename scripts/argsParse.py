# coding:utf-8
# @Time  : 2019-08-16 18:13
# @Author: Xiawang
# Description:

class argsParse:
    def __init__(self, schema, args):
        self.schema = schema
        self.args = args

    def assert_flag_type(self, flag):
        if '-' + flag in self.args and flag in self.schema:
            flag_type, flag_default_value, flag_description = self.schema[flag]
            flag_value = self.args['-' + flag]
            try:
                flag_value = eval('{}({})'.format(flag_type, flag_value))
            except ValueError:
                return False
            if isinstance(flag_value, eval(flag_type)):
                return True
        return False
