from myProject import DBClass as con

class Bank:

    obj=con()
    total_balance=2000
    def __init__(self):
        
        # self.registrationForm()
        self.home()
        # self.choice()

    def home(self):
        print("********walecome to SjBack********")
        print()
        print("1) login ")
        print("2) regirationFrom")
        
        open=input("choose the opration:--")
        if open=="2":
            self.registrationForm()
        elif open=="1":
            self.login()
        else:
            print("put the valid input")
            return self.home()
        

    #ragister page
    def registrationForm(self):
        self.name=input("enter the name:-")
        self.password=input("enter the password:-")
        self.obj.createAccount(self.name,self.password)

        return self.login()

    # login page
    def login(self):
        print("------walecome to the login page-----")
        print()
        self.username=input("enter the name:-  ")
        self.password=input("enter the password:- ")
        access=self.obj.fatchName_password(self.username,self.password)
        
        acc=list(access)[0]
        print(acc)
        l=[]
        
        adminname="admin"
        password="8689"
        if access == l:
            print("try age")
            self.login()

        elif adminname==acc[0] and password==acc[1]:
            self.Adminchoice()
                
        elif self.username==acc[0] and self.password==acc[1]:
            print("your login successully")
            self.choice()
            
        else:
            print("hlle")
            

    # self_user_check_Balance            
    def selfBalance(self):
        access=self.obj.fatchName_password(self.username,self.password)
        for i in access:
            print('name:-',i[0])
            # print('password:-',i[1])
            print('accountNO:- ',i[2])
            print('total balance:-',i[3])
              
    # self withdrowal
    def withrowal(self,amount):
        
        access=self.obj.fatchName_password(self.username,self.password)
       
        for i in access:
            
            conve=int(i[3])
            if conve>=amount:
                hold=conve-amount
                self.obj.UpdateAmount(hold,i[2])
                print(i[0],"your total value:-",hold)
            else:
                print(" tere ko jitna amount chaliye utna tere account me haich nhi bantaye tere account me shirf: -     ",i[3])
        
    #    chack the balance
    def balance(self):
        '''totol ballance in  the account'''
        fatch=self.obj.fatchValua()
        for i in fatch:
            print('name:-',i[1])
            print('password:-',i[2])
            print('accountNO:- ',i[3])
            print('total balance:-',i[4])
            print('*******************')
            print()
        # print(self.name,"your total balance:-",self.total_balance)

    def deposite(self,amount):
        access=self.obj.fatchName_password(self.username,self.password)

        for i in access:
            hold=int(i[3])+amount
            self.obj.UpdateAmount(hold,i[2])
            print(i[0],"your total value:-",hold)
            
    #change the password only for user
    def changePasswordOnly(self,newpassword):
        self.obj.changeThepasword(newpassword,self.password)
        print("succesefully change password")
        
    # access admin only
    def Adminchoice(self):
        print("walecome to admin")
        print('''1) show all account 
            2) delete the account
            3) update the account
            4) logout   ''')
        task=input("enter the task:-")
        if task=="1":
            self.balance()
            return self.Adminchoice()
        elif task=="2":
            acNO=input("enter the accountNo :- ")
            self.obj.deleteForAccount(acNO)
            return self.Adminchoice()
        elif task=="3":
            name=input("enter the newName:- ")
            password=input("enter the newPassword:- ")
            accountNo=input("user account number:-")
            self.obj.updateValue(name,password,accountNo)
            return self.Adminchoice()
        
        elif task=="4":
            print("succesfully logout")
            return self.login()
        else:
            print("enter the valid input and try agen")
            return self.Adminchoice()


    
    #access the user 
    def choice(self):
        while True:
            print('1) balance')
            print('2) withdrowl')
            print("3) Deposite")
            print("4) change password ")
            print("5  ) exit")

            input1=input("enter the task:-")
            if input1=="1":
                # self.balance()
                self.selfBalance()

            elif input1=="2":
                try:
                    with_value=int(input("enter the withrowale vlaue: -"))
                    if with_value>0:
                        self.withrowal(with_value)
                        # self.balance()

                    else :
                        print(self.name,"nagative value not valud")
                except ValueError:
                    print("put the valid input")

            elif input1=="3":
                try:
                    dep_value=int(input("enter the deposit value:-"))
                    if dep_value>=0:
                        self.deposite(dep_value)
                        # self.balance()
                    else:
                        print("nagative amount not be alwout")
                except ValueError :
                    print("put the valid input")

            elif input1=="4":
                newPassword=input('enter the new password:- ')
                self.changePasswordOnly(newPassword)
            elif input1=="5":
                break
                print("your logout successully")
            # elif input1==("-inf"):
            #     print("invalid input")

            else :
                print("invalid task: and choice the task agen")


# create the object
obj=Bank()


        
        
