from tkinter import *
from tkinter import ttk

def sign_up():
    password = Entry.get()
    print("Password:", password)

root = Tk()
root.geometry("300x300")
root.title("Sign-Up") 

signinButton = ttk.Entry(root)

labl1 = ttk.Label(root,text = "Name:")
labl1.grid(row = 0,column = 0)

labl2 = ttk.Label(root,text = "Email:")
labl2.grid(row = 1,column = 0)

labl3 = ttk.Label(root,text = "Password:")
labl3.grid(row = 2,column = 0)

btn4 = ttk.Button(root,text = "Sign-up Now")
btn4.grid(row = 3,column = 1)
signinButton = ttk.Button(root, text = "Sign-up", command = sign_up)

entry1 = ttk.Entry(root,text = "Name")
entry1.grid(row = 0,column = 1)

entry2 = ttk.Entry(root,text = "Email")
entry2.grid(row = 1,column = 1)

entry2 = ttk.Entry(root,text = "Password")
entry2.grid(row = 2,column = 1)



root.mainloop()