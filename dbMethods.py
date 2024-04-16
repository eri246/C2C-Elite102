import mysql.connector
import tkinter


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
    return mycursor.fetchall()
    

def withdraw(id, amount):
   currentAmount = getBalance(id)
   newAmount = currentAmount - amount
   if newAmount < 0:
    return None
   sql = "UPDATE user_accounts SET account_balance = {newAmount} WHERE id = {id}"
   mycursor.execute(sql)
   conn.commit()
   return newAmount

def deposit(id, amount):
   currentAmount = getBalance(id)
   newAmount = currentAmount + amount
   sql = "UPDATE user_accounts SET account_balance = {newAmount} WHERE id = {id}"
   mycursor.execute(sql)
   conn.commit()
   return newAmount

def updatePassword(id, oldPassword, newPassword):
    mycursor.execute( f'SELECT account_balance FROM user_accounts WHERE id = {id}')
    dbPassword = mycursor.fetchall()
    conn.commit()
    if(oldPassword != dbPassword):
       return False
    sql = "UPDATE user_accounts SET pasword = {newPassword} WHERE id = {id}"
    mycursor.execute(sql)
    conn.commit()
    return True

def signIn(fname, lname, password):
    mycursor.execute( f'SELECT id FROM user_accounts WHERE user_first_name = {fname}, user_last_name = {lname}, password = {password}')
    clientId = mycursor.fetchone()[0]

   
   




    


