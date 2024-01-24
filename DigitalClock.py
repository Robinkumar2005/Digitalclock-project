from tkinter import *
from time import strftime

window= Tk()
window.resizable(0,0)
window.title("Digital Clock")

def time():
    a=strftime("%H:%M:%S %p \n %D")
    Label.config(text=a)
    Label.after(1000,time)
Label=Label(window,font=("calibri", 50,"bold"),background="grey", foreground="white")
Label.pack(anchor="center")
time()
window.mainloop()