import mysql.connector as connection
import random


class DBClass:
    balance=2000
    def __init__(self):
        self.conn=connection.connect(host='localhost', port='3306', username='root', password='root' , database="pythonproject")
        
        query="create table if not exists SJBank(userid int NOT NULL AUTO_INCREMENT, userName varchar(50), password varchar(50), accountNo varchar(15) , balance varchar(100) , primary key(userid))"
        cur=self.conn.cursor()
        cur.execute(query)
        print("create")


    # # create the account
    # def createAccount(self,name,password):
    #     # self.balance=2000
    #     self.n=n = random.randint(1001,2000)
    #     query="insert into SJBank(userName, password,accountNO,balance) values('{}','{}','{}','{}')".format(name,password,n,self.balance)
    #     cur=self.conn.cursor()
    #     cur.execute(query)
    #     self.conn.commit()
    #     print("create the account")

    # fatche the value
    # def fatchValua(self):
    #     query="select * from sjbank"
    #     cor=self.conn.cursor()
    #     cor.execute(query)
    #     for i in cor:
    #         print('name:-',i[1])
    #         print('password:-',i[2])
    #         print('accountNO:- ',i[3])
    #         print('total balance:-',i[4])
    #         print('*******************')
    #         print()

    # DELETE VALUE
    def deleteForAccount(self,account):
        query='delete from sjbank where accountNO={}'.format(account)
        cur=self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        print("successfully delete this account:-",account)

    # update Value
    def updateValue(self,accno, name, password):
        query='update sjbank set userName="{}", password="{}" where accountNO="{}"'
        cur=self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        print('successfully update')
        


conn=DBClass()
# conn.fatchValua()
# conn.createAccount("jairuddin",'555')
# conn.deleteForAccount('1335')
conn.updateValue('1355','mysj','555')
