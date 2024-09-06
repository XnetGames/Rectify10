from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Radiobutton
from PIL import Image, ImageTk
import tkinter as tk
import subprocess
import os
import shutil
from PIL import Image, ImageTk, ImageSequence
from itertools import cycle

def on_closing():
    if messagebox.askokcancel("Выход из установки", "Хотите выйти из установки Rectify10?"):
        tk.destroy()

def change_text():
    global current_text_index
    current_text_index = (current_text_index + 1) % len(text_list)
    canvas.itemconfig(text_id, text=text_list[current_text_index])
    tk.after(5000, change_text)

def change_image():
    global current_image_index
    current_image_index = (current_image_index + 1) % len(image_list)
    img = ImageTk.PhotoImage(image_list[current_image_index])
    canvas.itemconfig(image_id, image=img)
    canvas.img = img
    tk.after(5000, change_image)

tk = Tk()
tk.protocol("WM_DELETE_WINDOW", on_closing)
tk.title("Установщик Rectify10")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=600, height=400, bd=0, highlightthickness=0)
canvas.pack()

text_list = ["Настройте Rectify в панели управления", "Производительность! В  буд. релизах", "Спасибо! За установку Rectify10 :)"]
current_text_index = 0
text_id = canvas.create_text(385, 150, text=text_list[current_text_index], font=("Arial", 15))

tk.after(5000, change_text)

image_list = [Image.open('cp.png'), Image.open('perf.png'), Image.open('cool.png')]
current_image_index = 0
img = ImageTk.PhotoImage(image_list[current_image_index])
image_id = canvas.create_image(30, 90, anchor=NW, image=img)
tk.after(5000, change_image)

canvas.create_text(45, 380, text="Install...", fill="black", font=("Arial", 15))

#Patcher

# Define the directory
directory = "C:/Windows/Rectify10/Colorizer"

# Create the directory
os.makedirs(directory, exist_ok=True)

# Define the directory
directory = "C:/Windows/Rectify10/ContextMenu"

# Create the directory
os.makedirs(directory, exist_ok=True)

# Define the directory
directory = "C:/Windows/Rectify10/Themes"

# Create the directory
os.makedirs(directory, exist_ok=True)

# Create the directory
os.makedirs(directory, exist_ok=True)

# Define the directory
directory = "C:/Windows/Rectify10/Themes/Mica"

# Create the directory
os.makedirs(directory, exist_ok=True)

# Define the directory
directory = "C:/Windows/Rectify10/Wallpepers"

# Create the directory
os.makedirs(directory, exist_ok=True)


def copy_file(source_path, destination_path):
    try:
        shutil.copy2(source_path, destination_path)
        print(f"Файл '{source_path}' скопирован в '{destination_path}'")
    except FileNotFoundError:
        print(f"Ошибка: Файл '{source_path}' не найден.")
    except Exception as e:
        print(f"Ошибка при копировании файла: {e}")

copy_file('AccentColorizer.exe', 'C:\\Windows\\Rectify10\\Colorizer')

def copy_file(source_path, destination_path):
    try:
        shutil.copy2(source_path, destination_path)
        print(f"Файл '{source_path}' скопирован в '{destination_path}'")
    except FileNotFoundError:
        print(f"Ошибка: Файл '{source_path}' не найден.")
    except Exception as e:
        print(f"Ошибка при копировании файла: {e}")

copy_file('AcrylicMenusLoader.exe', 'C:\\Windows\\Rectify10\\ContextMenu')

def copy_file(source_path, destination_path):
    try:
        shutil.copy2(source_path, destination_path)
        print(f"Файл '{source_path}' скопирован в '{destination_path}'")
    except FileNotFoundError:
        print(f"Ошибка: Файл '{source_path}' не найден.")
    except Exception as e:
        print(f"Ошибка при копировании файла: {e}")

copy_file('AcrylicMenus.dll', 'C:\\Windows\\Rectify10\\ContextMenu')

def copy_file(source_path, destination_path):
    try:
        shutil.copy2(source_path, destination_path)
        print(f"Файл '{source_path}' скопирован в '{destination_path}'")
    except FileNotFoundError:
        print(f"Ошибка: Файл '{source_path}' не найден.")
    except Exception as e:
        print(f"Ошибка при копировании файла: {e}")

copy_file('1.png', 'C:\\Windows\\Rectify10\\Wallpepers')

def copy_file(source_path, destination_path):
    try:
        shutil.copy2(source_path, destination_path)
        print(f"Файл '{source_path}' скопирован в '{destination_path}'")
    except FileNotFoundError:
        print(f"Ошибка: Файл '{source_path}' не найден.")
    except Exception as e:
        print(f"Ошибка при копировании файла: {e}")

copy_file('2.jpg', 'C:\\Windows\\Rectify10\\Wallpepers')

def copy_file(source_path, destination_path):
    try:
        shutil.copy2(source_path, destination_path)
        print(f"Файл '{source_path}' скопирован в '{destination_path}'")
    except FileNotFoundError:
        print(f"Ошибка: Файл '{source_path}' не найден.")
    except Exception as e:
        print(f"Ошибка при копировании файла: {e}")

copy_file('3.jpg', 'C:\\Windows\\Rectify10\\Wallpepers')

def copy_file(source_path, destination_path):
    try:
        shutil.copy2(source_path, destination_path)
        print(f"Файл '{source_path}' скопирован в '{destination_path}'")
    except FileNotFoundError:
        print(f"Ошибка: Файл '{source_path}' не найден.")
    except Exception as e:
        print(f"Ошибка при копировании файла: {e}")

copy_file('4.png', 'C:\\Windows\\Rectify10\\Wallpepers')

def copy_file(source_path, destination_path):
    try:
        shutil.copy2(source_path, destination_path)
        print(f"Файл '{source_path}' скопирован в '{destination_path}'")
    except FileNotFoundError:
        print(f"Ошибка: Файл '{source_path}' не найден.")
    except Exception as e:
        print(f"Ошибка при копировании файла: {e}")

copy_file('5.png', 'C:\\Windows\\Rectify10\\Wallpepers')

# Patch phase 2

def copy_file(source_path, destination_path):
    try:
        shutil.copy2(source_path, destination_path)
        print(f"Файл '{source_path}' скопирован в '{destination_path}'")
    except FileNotFoundError:
        print(f"Ошибка: Файл '{source_path}' не найден.")
    except Exception as e:
        print(f"Ошибка при копировании файла: {e}")

copy_file('Phase2.exe', 'C:\\Windows\\Rectify10\\')

os.startfile(r'C:\\Windows\\Rectify10\\Phase2')  

tk.mainloop()
