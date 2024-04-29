from tkinter import *
from tkinter import ttk
from dbMethods import *



def frameSetup(root):
    global frm
    frm = ttk.Frame(root, padding=10)
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
    Label(frm, text="Signing in: ", font=('Arial', 20)).grid(column=0, row=0)
    Label(frm, text="Enter Your First name here: ").grid(column=0, row=1)
    fname = Entry(frm)
    fname.grid(column=1, row=1)
    Label(frm, text="Enter Your Last name: ").grid(column=0, row=2)
    lname = Entry(frm)
    lname.grid(column=1, row=2)
    Label(frm, text="Enter your password here: ").grid(column=0, row=3)
    password = Entry(frm)
    password.grid(column=1, row=3)
    Button(frm, text="Press this button when details are all correct and you will be signed in", command= lambda: [signIn(fname.get(),lname.get(),password.get()),optionsMenu()]).grid(column=0, row=5)

def optionsMenu():
    clearFrame()
    Label(frm, text="Choose from list of options", font=('Arial', 20)).grid(column=0, row=0)
    Label(frm, text="Account Balance: " + str(getBalance(getClientId()))).grid(column=0, row=1)
    
def clearFrame():
    for widgets in frm.winfo_children():
        widgets.destroy()

