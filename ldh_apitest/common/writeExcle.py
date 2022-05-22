#coding=utf-8
from ldh_apitest.common.sql import make_dict,make_data
import pandas as pd
import time
import os

def writeExcle():
    sql='select * from web_apis'
    testData = make_dict(make_data(sql))
    currtime=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    df=pd.DataFrame(testData)
    file=os.path.dirname(os.getcwd())+ currtime+'.xlsx'
    df.to_excel(file, sheet_name='Sheet1', index=False,encoding='utf-8')
writeExcle()
# pd.set_option("display.max_columns",1000)
# pd.set_option("expand_frame_repr",False)
# pf=pd.read_excel('../data/kcb.xlsx')
# print(pf)
# pf.to_excel('1112xlsx','sheet名')