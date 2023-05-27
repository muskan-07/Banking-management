import pymysql
class connection1:
    def getconnection(self):
        try:
            conn=pymysql.connect(host='localhost',user='root',password='',db='bank' )
        except Exception as e:
            print(e)
        else:
            print("Connection successful")
            return conn
  
