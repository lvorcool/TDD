# coding:utf-8
# @Time  : 2020/4/2 21:27
# @Author: Xiawang
# Description:
import pytest

from scripts.demo0402 import flow_01


@pytest.mark.parametrize('a', [(1), (5)])
def test_flow_01(a):
    r = flow_01(a)
    assert r == a
