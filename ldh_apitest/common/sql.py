#coding=utf-8
import pymysql
con= pymysql.connect(host="127.0.0.1",port=3306,user="root",password="123aa",database="atp",autocommit=True)
cur=con.cursor()
def write_data():
    sql='''INSERT INTO `web_apis` (api_name,api_url,api_param_value,api_method,api_result,api_status,create_time,api_product_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s) '''
    sql1 = '''insert into `set`(set_name,set_value) values (%s,%s)'''
    cur.execute(sql1,('11','22'))
    cur.execute(sql,('测试登录-密码错误',
                     'https://gateway-dev.kcbxgk.com/sso/api/login',
                     'loginText = lidehui & loginPass = 123123aa',
                     'post',
                     'True',
                     '1',
                     '2022-05-09 03:54:39.505711',
                     '1'))

def make_data(sql):
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
    write_data()