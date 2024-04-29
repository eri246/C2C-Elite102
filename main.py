from tkinter import *
from tkinter import ttk
from dbMethods import *
from GUIMethods import *

    
    
root = Tk()


root.title("Welcome to Ericks Bank Service")
root.geometry("900x900")
root.minsize(800, 800)

frameSetup(root)
startScreenSetup()

"""
i = Entry(frm)
i.grid(column=0, row=4)

Label(frm, text="Log In").grid(column=0, row=0)

Button(frm, text='Quit',command=root.destroy).grid(column=1, row=0)
addNewUser = Button(frm, text='Add a new account', fg="blue",command=showStuff)



addNewUser.grid(column=1, row=2)"""
root.mainloop()
