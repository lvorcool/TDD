# coding:utf-8
# @Time  : 2019-08-16 17:32
# @Author: Xiawang
# Description:


class schemaParse:

    def __init__(self, schema_template):
        self.schema_template = schema_template

    def schema_parse(self):
        schema_list = self.schema_template.split(' ')
        schema_dict = {}
        for schema in schema_list:
            [flag_name, flag_type] = schema.split(':')
            schema_dict[flag_name] = eval(flag_type), eval('{}()'.format(flag_type)), '该参数 {} 的类型是 {}'.format(flag_name,
                                                                                                             flag_type)
        return schema_dict


if __name__ == '__main__':
    text = 'l:bool'
    re = schemaParse(text).schema_parse()
    print(re)
