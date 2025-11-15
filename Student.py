# install database library(my sql)
# pip install my sql(if you want to use  my sql. install this terminal)

import mysql. connector

conn =  mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "niit_2025"
)
cursor = conn.cursor()
info = "select * from student"
cursor.execute(info)
records = cursor.fetchall()
for i in records:
    print(i)
conn.close()