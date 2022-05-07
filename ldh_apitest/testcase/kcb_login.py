#! /usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
import requests
from ddt import ddt,data,unpack
from ldh_apitest.common.sendRequests import SendRequests
from ldh_apitest.common.readExcel import ReadExcel
import os
import json
path = os.path.dirname(os.getcwd())+"\\data\\kcb.xlsx"
testData = ReadExcel.readExcel(path,"Sheet1")

@ddt
class Test1(unittest.TestCase):
    def setUp(self):
        self.s = requests.session()

    @data(*testData)
    def test_kcblogin_api(self,data):
        re = SendRequests().sendRequests(self.s, data)
        result=str(json.loads(re.text)['success'])
        expect_result =eval(data["expect_result"].split(":")[1]).title()
        self.assertEqual(result, expect_result, "返回错误,实际错误码应是\t%s"%re.json()["success"])

if __name__ == '__main__':
    unittest.main()