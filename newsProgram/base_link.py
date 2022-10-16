import cursor as cursor
import pymysql as pymysql

import xlrd

# 连接数据库
# from django import db
from django.contrib.sessions.backends import db

conn = pymysql.connect(
    host='rm-uf6mav88a70rf99w3to.mysql.rds.aliyuncs.com',
    user='gaohan',
    password='GAOhan1234567',
    db='lualu',
    port=3306,
    charset='utf8'

    # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
)
# 创建游标对象 用来逐行获取查询数据 创建游标后 系统会将查询结果存放 游标就是取数据的接口 这里有两种方法获取结果集中的数据。
# 一个是fetchone()，该方法一次获取一条记录，每一条记录是一个元组形式的数据，每获取一条记录游标会往前移动一格，等待获取下一条记录；
# 一个是fetchall()方法，能够一次性的获取所有的数据，该方法返回的是一个元组列表。
# 当完成所有操作后，记得断开数据库的连接，释放资源。

cur = conn.cursor()
# cur.execute('SELECT * FROM `newtest`.`news` ')
# cur.execute('INSERT INTO news ( title) VALUES ( "长期233")')
# conn.commit()
# a = cur.fetchall()
# for i in a:
#     print(i[i])
# print(a)
cur.execute("""SELECT * FROM subway""")
# res1 = cur.fetchone()
# print(res1)
res = cur.fetchall()
print(len(res))
print(list[res])
a = (list[res])
# 关闭游标和数据库连接
cur.close()
