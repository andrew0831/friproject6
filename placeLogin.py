import tkinter as tk

def login():
    username = usernameEntry.get()
    password = passwordEntry.get()
    print("Username:", username)
    print("Password:", password)

root = tk.Tk()
root.title("Login")

usernameEntry = tk.Entry(root)
passwordEntry = tk.Entry(root, show="a")

usernameLabel = tk.Label(root, text = "Username:")
passwordLabel = tk.Label(root, text = "Password:")


loginButton = tk.Button(root, text = "Login", command = login)

usernameLabel.place(x=30, y=50)
passwordLabel.place(x=30, y=80)

usernameEntry.place(x=120, y=50)
passwordEntry.place(x=120, y=80)

loginButton.place(x=80, y=120)

root.mainloop()





