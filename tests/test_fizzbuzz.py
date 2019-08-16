# coding:utf-8
# @Time  : 2019-08-16 12:58
# @Author: Xiawang

import pytest
from scripts.fizzbuzz import fizzbuzz

class Test_test_fizzbuzz:
    @pytest.mark.parametrize("number,result", [(3, 'Fizz'),(5,'Buzz'),(15,'FizzBuzz'),(1,1)])
    def test_fizzbuzz(self, number, result):
        assert fizzbuzz(number).fizzbuzz() == result
