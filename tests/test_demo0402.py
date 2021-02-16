# coding:utf-8
# @Time  : 2020/4/2 21:27
# @Author: Xiawang
# Description:
import pytest

from scripts.demo0402 import flow_01, flow_02


@pytest.mark.parametrize('a', [(1), (5)])
def test_flow_01(a):
    r = flow_01(a)
    assert r == a


@pytest.mark.parametrize('b,expect_result', [(2, 4), (6, 8)])
def test_flow_02(b, expect_result):
    r = flow_02(b)
    assert r == expect_result
