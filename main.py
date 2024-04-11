from tkinter import *
from dbMethods import *
root = Tk()
w = Label(root, text=getBalance(1))
w.pack()
root.mainloop()
