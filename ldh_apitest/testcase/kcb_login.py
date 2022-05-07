#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
@version: 1.0
@author: ldh
@site:
@software: PyCharm
@file: case_01.py
@time: 2018/3/16 10:58
"""
import unittest
import requests
from ddt import ddt,data,unpack
from ldh_apitest.common.sendRequests import SendRequests
from ldh_apitest.common.readExcel import ReadExcel
import os

path = os.path.dirname(os.getcwd())+"\\data\\qq_apiTest.xlsx"
testData = ReadExcel.readExcel(path,"Sheet1")

@ddt
class Test1(unittest.TestCase):
    def setUp(self):
        self.s = requests.session()

    @data(*testData)
    def test_qq_api(self,data):
        re = SendRequests().sendRequests(self.s, data)
        expect_result =eval(data["expect_result"].split(":")[1])
        self.assertEqual(re.json()["reason"], expect_result, "返回错误,实际结果是%s"%re.json()["reason"])

if __name__ == '__main__':
    unittest.main()