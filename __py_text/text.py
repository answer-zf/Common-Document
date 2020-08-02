"""

"""

import pymysql

db = pymysql.connect(host="localhost", port=3306, user="root", passwd="341309", database="stu", charset="utf8")
cur = db.cursor()


class User_Operate:

    def _regist(self):
        while True:
            name = input("regist name: ")
            passwd = input("regist passwd: ")

            select_sql = "SELECT * FROM user WHERE name = %s"
            cur.execute(select_sql, [name])

            if cur.fetchone() == None:
                insert_sql = "INSERT INTO user (name,passwd) VALUES (%s,%s);"
                cur.execute(insert_sql, [name, passwd])
                print("Regist Complete!")
                break
            else:
                print("user name exist")

    def _login(self):
        while True:
            name = input("login name: ")
            passwd = input("login passwd: ")
            select_sql = "SELECT * FROM user WHERE name = %s AND passwd = %s;"
            cur.execute(select_sql, [name, passwd])
            if cur.fetchone() != None:
                print("login!!!")
                break
            else:
                print("error")

    def main(self):
        while True:
            str_item = input("""
                *************************
                        Regist: 1
                        Login:  2
                *************************
            """)
            if str_item == "1":
                self._regist()
            elif str_item == "2":
                self._login()


if __name__ == '__main__':
    operate = User_Operate()
    operate.main()
