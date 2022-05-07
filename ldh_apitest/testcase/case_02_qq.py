#! /usr/bin/env python
# -*- coding:utf-8 -*-

import unittest

import requests
from ddt import ddt,data,unpack
from ldh_apitest.common.sendRequests import SendRequests
from ldh_apitest.common.readExcel import ReadExcel
import os

#print(os.path.dirname(os.getcwd()))
path = os.path.dirname(os.getcwd())+"\\data\\qq_apiTest.xlsx"
print(path)
testData = ReadExcel.readExcel(path,"Sheet1")

@ddt
class Test1(unittest.TestCase):

    def setUp(self):
        self.s = requests.session()

    @data(*testData)
    def test_qq_api(self,data):

        re = SendRequests().sendRequests(self.s, data)
        #切割字符串取后面的部分
        expect_result1 = data["expect_result"].split(":")[1]
        #转换为字符串
        expect_result = eval(expect_result1)
        self.assertEqual(re.json()["reason"], expect_result, "返回错误,实际结果是%s"%re.json()["reason"])

if __name__ == '__main__':
    unittest.main()