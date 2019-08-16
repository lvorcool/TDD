# coding:utf-8
# @Time  : 2019-08-16 13:15
# @Author: Xiawang
# Description:


def add_demo(arg1,arg2):
    try:
        return arg1+arg2
    except TypeError:
        return "只能输入数字!"