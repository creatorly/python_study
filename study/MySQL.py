#python3不再支持mysqldb 请用pymysql和mysql.connector

import mysql.connector

conn = mysql.connector.connect(user='root', password='root', database='test')

cursor = conn.cursor()

#增加判断if not exists，不存在则调用
cursor.execute('create table if not exists user (id varchar(20) primary key, name varchar(20))')

cursor.execute("SHOW DATABASES")

for x in cursor:
  print(x)

cursor.execute("SHOW TABLES")
for x in cursor:
  print(x)

count = cursor.rowcount

#cursor.execute("alter table user ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

sql = "insert into user (id, name) values (%s, %s)"
val = ("RUNOOB4", "https://www.runoob.com")
cursor.execute(sql, val)

print(cursor.rowcount)
print(cursor.lastrowid)
cursor.execute("SELECT * FROM user")
values = cursor.fetchall()
print(values)

conn.commit()
cursor.close()
conn.close()