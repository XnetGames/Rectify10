from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Radiobutton  

def on_closing():
    if messagebox.askokcancel("Выход из установки", "Хотите выйти из установки Rectify10?"):
        tk.destroy()

tk = Tk()
tk.protocol("WM_DELETE_WINDOW", on_closing)
tk.title("Установщик Rectify10")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=600, height=400, bd=0, highlightthickness=0)
canvas.pack()

our_image = PhotoImage(file="incomplete.png")
our_label = Label(tk, image=our_image)
our_label.place(x=5, y=85)

canvas.create_text(360, 70, text="Добро пожаловать!", fill="black", font=("Arial", 20))
canvas.create_text(370, 120, text="Нужных для Rectify10", fill="black", font=("Arial", 15))
canvas.create_text(410, 100, text="Установка пройдет в 2 этапа, ", fill="black", font=("Arial", 15))

tk.mainloop()
