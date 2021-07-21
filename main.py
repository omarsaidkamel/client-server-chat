import tkinter as tk
import socket
from tkinter import *
from tkinter import ttk

Massage = []
i = 0

# function of send massage
def send(event):
    global i
    result = str.capitalize(name.get())
    # print(result)
    try:
        text.delete(0, END)
    except:
        print("error")
    Massage.append(result)
    i += 1
    label = tk.Label(frame, text=result)
    label.place(relx=0.01, rely=i / 10)


def Send():
    global i
    result = str.capitalize(name.get())
    # print(result)
    try:
        text.delete(0, END)
    except:
        print("error")
    Massage.append(result)
    i += 1
    label = tk.Label(frame, text=result)
    label.place(relx=0.01, rely=i / 10)


def receive():
    global i
    result = str.capitalize(name.get())
    # print(result)
    try:
        text.delete(0, END)
    except:
        print("error")
    i += 1
    Massage.append(result)
    label = tk.Label(myfram, text=result)
    label.pack()
    #label.place(relx=0.8, rely=i / 10)


root = tk.Tk()
root.bind('<Return>', send)
root.title("Chat Program")
root.iconbitmap('chat.ico')
root.geometry("400x400")

frame = tk.Frame(root, bg="white")
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

# Text Box
name = StringVar()
text: Entry = Entry(root, width=54, textvariable=name)
text.place(relx=0.01, rely=0.9)

# send Button
sendBTN = ttk.Button(root, text="Send", command=receive)
sendBTN.place(relx=0.8, rely=0.9)

# Run The Form
root.mainloop()
