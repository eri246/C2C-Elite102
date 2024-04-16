from tkinter import *
from tkinter import ttk

def startScreenSetup(frm):
    
    Label(frm, text="This is my very proffesional bank").grid(column=0, row=0)
    signInButton = Button(frm, text="Press this button to sign in").grid(column=0, row=1)
    addAccountButton = Button(frm, text="Press this button to make an account").grid(column=0, row=2)
   

def createAccountScreen(frm):
    
    Label(frm, text="Enter Your First name here").grid(column=0, row=0)

def createSignInScreen(frm):
    
    Label(frm, text="Enter Your First name here").grid(column=0, row=0)

def clearFrame(frm):
    for widget in frm.winfo_children():
        widget.destroy()