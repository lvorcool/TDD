# coding:utf-8
# @Time  : 2019-08-16 13:11
# @Author: Xiawang

import pytest
from scripts.add_demo import add_demo

class Test_test_add:
    def test_add(self ):
        assert add_demo(3,5) == 8


