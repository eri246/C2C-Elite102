import mysql.connector
import tkinter
from decimal import Decimal


conn = mysql.connector.connect(
    user='root',
    host='localhost',
    password='Dog=cat6',
    database = "c2cproject"
)


mycursor = conn.cursor()

addId = 0
clientId = 0

def getAddId():
   mycursor.execute("SELECT MAX(id) FROM user_accounts")
   return mycursor.fetchone()[0]

def addNewUser(fname,lname,accountBalance,password):
    addId = 1 + getAddId()
    sql = "INSERT INTO user_accounts (id, user_first_name, user_last_name, account_balance, password) VALUES (%s, %s, %s, %s, %s)"
    mycursor.execute(sql, (addId, fname, lname, accountBalance, password))
    conn.commit()

def getBalance(id):
    sql = f'SELECT account_balance FROM user_accounts WHERE id = {id}'
    mycursor.execute(sql)
    balance = mycursor.fetchone()[0]
    return balance
    

def withdraw(id, amount):
   currentAmount = getBalance(id)
   newAmount = Decimal(currentAmount) - Decimal(amount)
   if newAmount < 0:
    return None
   sql = f"UPDATE user_accounts SET account_balance = {newAmount} WHERE id = {id}"
   mycursor.execute(sql)
   conn.commit()
   return newAmount

def deposit(id, amount):
   currentAmount = getBalance(id)
   newAmount = Decimal(currentAmount) + Decimal(amount)
   sql = f"UPDATE user_accounts SET account_balance = {newAmount} WHERE id = {id}"
   mycursor.execute(sql)
   conn.commit()
   return newAmount

def updatePassword(id, oldPassword,newPassword):
    mycursor.execute( f'SELECT password FROM user_accounts WHERE id = {id}')
    dbPassword = mycursor.fetchone()[0]
    conn.commit()
    if(oldPassword != dbPassword):
       print("works")
       return False
    sql = f"UPDATE user_accounts SET password = '{newPassword}' WHERE id = {id}"
    mycursor.execute(sql)
    conn.commit()
    return True

def signIn(fname, lname, password):
    mycursor.execute(f"SELECT id FROM user_accounts WHERE user_first_name = '{fname}' AND user_last_name = '{lname}' AND password = '{password}'")
    global clientId
    pleaseWork =mycursor.fetchone()
    if  pleaseWork == None:
        return False
    else:
       clientId = pleaseWork[0]
       return True

def getClientId():
   return clientId





   
   




    


