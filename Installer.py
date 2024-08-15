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

our_image = PhotoImage(file = "incomplete.png")
our_label = Label(tk)
our_label.image = our_image
our_label['image'] = our_label.image
our_label.place(x = 10, y = 70)

canvas.create_text(360,70,tex="Добро пожаловать!",fill="black",font=(100))
canvas.create_text(395,95,tex="Установка будет в 2 этапа,",fill="black",font=(10))
canvas.create_text(370,120,tex="Нужных для Rectify10",fill="black",font=(100))

tk.mainloop()
