# coding:utf-8
# @Time  : 2019-08-16 13:02
# @Author: Xiawang
# Description:


class fizzbuzz:
    def __init__(self,number):
        self.number = number

    def fizzbuzz(self):
        if self.number % 3 ==0:
            return 'Fizz'
        if self.number % 5 ==0:
            return 'Buzz'