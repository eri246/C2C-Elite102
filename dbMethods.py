import mysql.connector
import tkinter

conn = mysql.connector.connect(
    user='root',
    host='localhost',
    password='Dog=cat6',
    database = "c2cproject"
)

mycursor = conn.cursor()

def addNewUser(id, fname,lname,accountBalance,password):
    sql = "INSERT INTO user_accounts (id, user_first_name, user_last_name, account_balance) VALUES (%s, %s, %s, %s, %s)"
    mycursor.execute(sql, (id, fname, lname, accountBalance, password))
    conn.commit()

def getBalance(id):
    sql = f'SELECT account_balance FROM user_accounts WHERE id = {id}'
    mycursor.execute(sql)
    return mycursor.fetchall()
    conn.commit()

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





    


