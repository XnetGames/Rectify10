from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Radiobutton
from PIL import Image, ImageTk
import tkinter as tk
import subprocess

def on_closing():
    if messagebox.askokcancel("Выход из установки", "Хотите выйти из установки Rectify10?"):
        tk.destroy()

def switch_image():
    global photo
    if photo == photo1:
        photo = photo3
    else:
        photo = photo1
    label.config(image=photo)

tk = Tk()
tk.protocol("WM_DELETE_WINDOW", on_closing)
tk.title("Установщик Rectify10 v1.0")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=600, height=400, bd=0, highlightthickness=0)
canvas.pack()

canvas.create_text(360, 70, text="Добро пожаловать!", fill="black", font=("Arial", 20))
canvas.create_text(370, 120, text="Нужных для Rectify10", fill="black", font=("Arial", 15))
canvas.create_text(410, 100, text="Установка пройдет в 2 этапа, ", fill="black", font=("Arial", 15))

# Load the images
image1 = Image.open("incomplete.png")
photo1 = ImageTk.PhotoImage(image1)
image3 = Image.open("installoptns.png")
photo3 = ImageTk.PhotoImage(image3)

# Set the initial image
photo = photo1

# Create a label to display the image
label = Label(tk, image=photo)
label.image = photo  # keep a reference!

# Place the label at a certain position
label.place(x=5, y=85)

def execute_commands():
    switch_image()
    run_script()
    # Add your second command here
    print("Second command executed")

def run_script():
    subprocess.run(["python", "installerwindow2.py"])

# Modify the button command to execute the new function
button = ttk.Button(tk, text="Установить", command=execute_commands)
button.pack()

tk.mainloop()
