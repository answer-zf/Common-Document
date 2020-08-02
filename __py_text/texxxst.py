import pymysql

db = pymysql.connect(host="localhost", port=3306, user="root", password="341309", database="stu", charset="utf8")
cur = db.cursor()

sql = "SELECT * FROM Images WHERE filename = 'MySQL.pdf';"
cur.execute(sql)

file_data = cur.fetchall()[0]

with open(file_data[1], "wb") as fd:
    fd.write(file_data[2])

cur.close()
db.close()
# create table Images (id int primary key auto_increment,filename varchar(16),data mediumblob);