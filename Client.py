from tkinter import *
import socket
from threading import Thread
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))


def send():
    massage = name.get()
    s.send(massage.encode("utf-8"))
    enter_text_widget.delete(0, END)
    chat_transcript_area.insert('end', 'Me : ' + massage + '\n')


root = Tk()
root.title("Client-Chat Program")
root.iconbitmap('chat.ico')
root.resizable(0, 0)
root.geometry("600x350")


frame = Frame()
Label(frame, text='Chat Box:', font=("Serif", 12)).pack(side='top', anchor='w')
chat_transcript_area = Text(frame, width=60, height=10, font=("Serif", 12))
scrollbar = Scrollbar(frame, command=chat_transcript_area.yview, orient=VERTICAL)
chat_transcript_area.config(yscrollcommand=scrollbar.set)
chat_transcript_area.bind('<KeyPress>', lambda e: 'break')
chat_transcript_area.pack(side='left', padx=10)
scrollbar.pack(side='right', fill='y')
frame.pack(side='top')


frame = Frame()
Label(frame, text='Enter message:', font=("Serif", 12)).pack(side='top', anchor='w')
name = StringVar()
enter_text_widget = Entry(frame, textvariable=name, font=("Serif", 12))
enter_text_widget.pack(side='left', pady=15)
join_button = Button(frame, text="Send", width=10, command=send).pack(side='left')
frame.pack(side='top')


def recvThread(h):
    while True:
        msg = h.recv(1024).decode("utf-8")
        chat_transcript_area.insert('end', msg + '\n')


t = Thread(target=recvThread, args=(s,))
t.start()
root.mainloop()
