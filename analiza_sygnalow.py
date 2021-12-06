from tkinter import messagebox
from tkinter import *
import tkinter as tk
import time
import random

window = tk.Tk()
window.title("Alfabet")
window.geometry('1200x1000')
window.config(bg = '#FFFFFF')



tytul = tk.Label(window, text = "Instrukcja", size = 30)
instrukcja = tk.Label(window, text = "Przed Tobą znajdzię się cały polski alfabet. Litery będa pojawiać się po kolei w odstępie czasowym jednej sekundy. Kliknij przycisk, aby rozpocząć.", size = 20)

b1 = Button(window, text = "Rozpocznij")
b2 = Button(window, text = "Wyjdź")

tytul.pack()
instrukcja.pack()
b1.pack()
b2.pack()

window.mainloop()
