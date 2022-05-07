#! /usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
import time
import os
from ldh_apitest.common.HTMLTestRunner_jpg import HTMLTestRunner

def run_case():
    case_dir = os.path.dirname(os.getcwd()) + "\\" + "testcase"
    test_case = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir,pattern="kcb_login.py",top_level_dir=None)
    return discover

if __name__ == '__main__':
    current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    report_path = os.path.dirname(os.getcwd()) + "\\report\\" + current_time + '.html'  # 生成测试报告的路径
    fp = open(report_path, "wb")
    runner = HTMLTestRunner(stream=fp, title=u"自动化测试报告", description=u'qq接口',verbosity=2)
    runner.run(run_case())
    fp.close()