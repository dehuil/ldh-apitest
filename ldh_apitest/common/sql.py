#coding=utf-8
import pymysql


def make_data(sql):
    con= pymysql.connect(host="127.0.0.1",port=3306,user="root",password="123aa",database="atp",autocommit=True)
    cur=con.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    con.close()
    return result

def make_dict(result):
    l3=[]
    l2=['id','name','method','url','params','headers','body','ytype','status_code','expect_result','msg']
    for i in result:
        l3.append(dict(zip(l2,i)))
    return l3

if __name__ == '__main__':
    print(make_dict(make_data('select * from excle')))