from tkinter import *
from tkinter import ttk
from dbMethods import *



def frameSetup(root):
    global frm
    frm = ttk.Frame(root, padding=5)
    frm.grid()
    
    
def startScreenSetup():
    clearFrame()
    Label(frm, text="This is my very professional bank", font=('Arial', 20)).grid(column=0, row=0)
    Button(frm, text="Press this button to sign in",command=createSignInScreen).grid(column=0, row=1)
    Button(frm, text="Press this button to make an account",command=createAccountScreen).grid(column=0, row=2)
   

def createAccountScreen():
    clearFrame()
    Label(frm, text="Creating an account: ", font=('Arial', 20)).grid(column=0, row=0)
    Label(frm, text="Enter Your First name here: ").grid(column=0, row=1)
    fname = Entry(frm)
    fname.grid(column=1, row=1)
    Label(frm, text="Enter Your Last name : ").grid(column=0, row=2)
    lname = Entry(frm)
    lname.grid(column=1, row=2)
    Label(frm, text="Enter Your account balance here: ").grid(column=0, row=3)
    balance = Entry(frm)
    balance.grid(column=1, row=3)
    Label(frm, text="Enter your password here: ").grid(column=0, row=4)
    password = Entry(frm)
    password.grid(column=1, row=4)
    Button(frm, text="Press this button when details are all correct and your account will be created", command= lambda: [addNewUser(fname.get(),lname.get(),balance.get(),password.get()), startScreenSetup()]).grid(column=0, row=5)

def createSignInScreen():
    clearFrame()
    Label(frm, text="Signing in - if details are incorrect you will remain on this window: ", font=('Arial', 20)).grid(column=0, row=0)
    Label(frm, text="Enter Your First name here: ").grid(column=0, row=1)
    fname = Entry(frm)
    fname.grid(column=1, row=1)
    Label(frm, text="Enter Your Last name: ").grid(column=0, row=2)
    lname = Entry(frm)
    lname.grid(column=1, row=2)
    Label(frm, text="Enter your password here: ").grid(column=0, row=3)
    password = Entry(frm)
    password.grid(column=1, row=3)
    Button(frm, text="Press this button when details are all correct and you will be signed in", command= lambda: [signInHelper(fname.get(),lname.get(),password.get())]).grid(column=0, row=5)
    Button(frm, bg='red',width=30, height=3, text="Press this button to return to start screen", command= lambda: [startScreenSetup()]).grid(column=0, row=7)


def optionsMenu():
    clearFrame()
    Label(frm, text="Choose from list of options", font=('Arial', 20)).grid(column=0, row=0)
    Label(frm, text="Account Balance: " + str(getBalance(getClientId()))).grid(column=0, row=1)
    
    Label(frm, text="Enter Amount of money to deposit: ").grid(column=0, row=2)
    depositAmount = Entry(frm, )
    depositAmount.grid(column=1, row=2)
    Button(frm, text="Press this button to deposit the money", command= lambda: [deposit(getClientId(), depositAmount.get()), optionsMenu()]).grid(column=2, row=2)
    
    Label(frm, text="Enter Amount of money to Witdhraw: ").grid(column=0, row=3)
    withdrawAmount = Entry(frm)
    withdrawAmount.grid(column=1, row=3)
    Button(frm, text="Press this button to witdhraw the money", command= lambda: [withdraw(getClientId(), withdrawAmount.get()), optionsMenu()]).grid(column=2, row=3)

    Label(frm, text="Password Settings - if your old password is incorrect you will remain on this window: ").grid(column=0, row=5)
    oldPassword = Entry(frm,width=30)
    oldPassword.insert(0,'Enter your old Password here')
    oldPassword.grid(column=0, row=6)
    newPassword = Entry(frm, width=30)
    newPassword.insert(0,'Enter your new Password here')
    newPassword.grid(column=1, row=6)
    Button(frm, text="Press this button to Update Password", command= lambda: [passwordHelper(oldPassword.get(), newPassword.get())]).grid(column=2, row=6)
    Label(frm, text="When you update your password you will have to sign in again").grid(column=0, row=7)
    
    Button(frm,bg='red',width=23, height=5, text="Press this button to sign out", command= lambda: [startScreenSetup()]).grid(column=0, row=9)


def passwordHelper(oldPassword, newPassword):
    if(updatePassword(getClientId(), oldPassword, newPassword)):
        createSignInScreen()


def signInHelper(fname, lname, password):
    if(signIn(fname, lname, password)):
        optionsMenu()
    

    



    
def clearFrame():
    for widgets in frm.winfo_children():
        widgets.destroy()

