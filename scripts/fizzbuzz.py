# coding:utf-8
# @Time  : 2019-08-16 13:02
# @Author: Xiawang
# Description:


class fizzbuzz:
    def __init__(self, number):
        self.number = number

    def fizzbuzz(self):
        result = ''
        if self.number % 3 == 0:
            result += 'Fizz'
        if self.number % 5 == 0:
            result += 'Buzz'
        return self.number if result == '' else result
