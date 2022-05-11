#coding=utf-8
import pymysql

def make_data():
    con= pymysql.connect(host="127.0.0.1",port=3306,user="root",password="123aa",database="atp",autocommit=True)
    cur=con.cursor()
    sql_1 = "select * from excle"
    cur.execute(sql_1)
    result_2 = cur.fetchall()    # 查询所有数据
    result_3 = cur.fetchmany(size=1)
    l=[]
    l3=[]
    l2=['id','name','method','url','params','headers','body','ytype','status_code','expect_result','msg']
    for i in result_2:
        l3.append(dict(zip(l2,i)))
    con.close()
    return l3

if __name__ == '__main__':
    print(make_data())
    for i in make_data():
        print(i['method'])