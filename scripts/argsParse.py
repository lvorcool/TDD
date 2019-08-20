# coding:utf-8
# @Time  : 2019-08-16 18:13
# @Author: Xiawang
# Description:

class argsParse:
    def __init__(self, schema, args):
        self.schema = schema
        self.args = args

    def set_args_value(self, flag, flag_value):
        self.args['-' + flag] = flag_value
        return self.args

    def assert_flag_type(self, flag):
        if '-' + flag in self.args and flag in self.schema:
            flag_type, flag_default_value, flag_description = self.schema[flag]
            flag_value = self.args['-' + flag]
            try:
                if not isinstance(flag_value, eval(flag_type)):
                    flag_value = eval('{}({})'.format(flag_type, flag_value))
                    self.set_args_value(flag, flag_value)
            except ValueError:
                return False
            if isinstance(flag_value, eval(flag_type)):
                return True
        return False

    def assert_flag_consistent(self):
        if not len(self.schema) == len(self.args):
            return False
        for flag in self.args:
            if flag[1:] in self.schema:
                continue
            else:
                return False
        return True

    def get_flag_value(self, flag):
        if self.assert_flag_type(flag) and self.assert_flag_consistent():
            return self.args['-' + flag]
        else:
            return self.schema[flag][2]
