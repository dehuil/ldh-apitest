#! /usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
import time
import os
from ldh_apitest.common.HTMLTestRunner_jpg import HTMLTestRunner

def run_case():
    case_dir = os.path.dirname(os.getcwd()) + "\\" + "testcase"
    test_case = unittest.TestSuite()
    return unittest.defaultTestLoader.discover(case_dir,pattern="kcb_login.py",top_level_dir=None)

if __name__ == '__main__':
    current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    report_path = os.path.dirname(os.getcwd()) + "\\report\\" + current_time + '.html'  # 生成测试报告的路径
    with open(report_path,'wb') as f:
        HTMLTestRunner(stream=f, title=u"自动化测试报告", description=u'kcb接口测试', verbosity=2).run(run_case())