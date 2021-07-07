import tkinter as tk
import socket


def online():
    cli = socket.socket()
    cli.connect(("127.0.0.1", 10000))
    cli.send(b"washer2")
    cli.send(b"ON")
    cli.close()


def offline():
    cli = socket.socket()
    cli.connect(("127.0.0.1", 10000))
    cli.send(b"washer2")
    cli.send(b"OFF")
    cli.close()


window = tk.Tk()

on = tk.Button(text="ONLINE", command=online)
off = tk.Button(text="OFFLINE", command=offline)

on.pack()
off.pack()

window.mainloop()