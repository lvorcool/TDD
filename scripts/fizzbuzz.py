# coding:utf-8
# @Time  : 2019-08-16 13:02
# @Author: Xiawang
# Description:


class fizzbuzz:
    def __init__(self, number):
        self.number = number

    def fizzbuzz(self):
        result = ''
        if self.is_divisible_or_is_contain(3):
            result += 'Fizz'
        if self.is_divisible_or_is_contain(5):
            result += 'Buzz'
        return self.number if result == '' else result

    def is_divisible_or_is_contain(self,arg):
        return self.number % arg ==0 or str(arg) in str(self.number)
