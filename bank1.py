import connection as c
from datetime import date as d

class registration:
    def gets(self):
        try:
            self._name=input("Enter your name:")
        except Exception as e:
            print(e,"input error")
        else:
            print(self._name)
            
                       
        self._acc=int(input("enter your account no.:"))
        self._dob=int(input("enter your age:"))
        self._city=input("Enter your city:")
        self._m=int(input("enter your mobile_no.:"))
        self._bal=500
    def show(self):
         print("name:",self._name)
         print("account number:",self._acc)
         print("date of birth:",self._dob)
         print("city:",self._city)
         print("mobile number:",self._m) 

class deposit:
    def gets(self):
        #print("Account no.",self._acc)
        #self._acc=int(input("enter your account no."))
        self._amt=int(input("enter deposit amount:"))
        
    def show(self):
        print("your account no.:",self._acc)
        print("deposit amount:",self._amt)

class Withdrawal:
    def gets(self):
        print("Account no.:",self._acc)
        #self._acc=int(input("enter your account no."))
        self._amt=int(input("enter withdrawal amount:"))
    def show(self):
        print("your account no.:",self._acc)
        print("withdrawal amount:",self._amt)

class Result(registration,deposit,Withdrawal):
    def compute(self):
        registration.gets(self)
        ch=input("enter debit-d or credit-c:")
        ch=ch.lower()
        self._tdate=str(d.today())
        if ch=='c':
            self._ttran=ch
            deposit.gets(self)

            self._bal=self._bal+self._amt
            self._rem="Creadit Amt Successfully"
        elif ch=='d':
            self._ttran=ch
            Withdrawal.gets(self)
            if self._bal>self._amt:
                self._bal=self._bal-self._amt
                print("balance:",self._bal)
                self._rem="Debit AMt Successfully"
            else:
                print("insufficiant balance:",self._bal)
                self._rem="No Transaction ,Insufficient balamance"
                  
        else:
            print("invalid transaction")

    def insertion(self):
        #create the object of class
        c1=c.connection1()
        conn=c1.getconnection()
        #create cursor
        cur=conn.cursor()
        query="insert into bankmanage values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val=(self._name,self._acc,self._dob ,self._city,self._m,self._bal,self._ttran,self._amt,self._tdate,self._rem)
        try:    
            cur.execute(query,val)
        except Exception as e1:
            print("query error")
        else:    
            conn.commit()
            print("record save successfully")
            conn.close()
    ''''def search(self):
          c1=c.connection1()
          conn=c1.getconnection()
          #creat cursor
          cur=conn.cursor()
          i=int(input("enter account no.:"))
          query="select*from bankmanage where acon=%s"
          cur.execute(query,i)
          ans=cur.fetchall()
          if ans:
              print(ans)
          else:
              print("account doesnt exist")
          conn.close()  '''  


#main program
        
res=Result()
res.compute()
res.insertion()
'''
#print("1.deposit amount")
#print("2.withdrawal amount")
#print("3.search account detail")
ch=int(input("enter your choice:"))
if ch==1:
    res.compute()
    res.insertion()
#elif ch==3:
    #res.search()
    '''
    
        
        

        


        

