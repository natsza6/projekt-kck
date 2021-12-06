from tkinter import messagebox
from tkinter import *
import tkinter as tk
import time
import random
import tkinter.font as font

window = tk.Tk()
window.title("Alfabet")
window.geometry('1000x700')
window.config(bg = '#FFFFFF')

def widget_destroy(widget):
    widget.destroy()

def b1_akcja():
    widget_destroy(tytul)
    widget_destroy(instrukcja)
    widget_destroy(b1)
    widget_destroy(b2)

def b2_akcja():
    window.destroy()

myFont1 = font.Font(family='Helvetica', size=50, weight='bold')
myFont2 = font.Font(family='Helvetica', size=30, weight='normal')

tytul = tk.Label(window, text = "Instrukcja")
instrukcja = tk.Label(window, text = "Przed Tobą znajdzię się cały polski alfabet. \n Litery będa pojawiać się po kolei w odstępie czasowym jednej sekundy. \n Mrugnij, jeśli chcesz wybrać literę. \n Kliknij przycisk, aby rozpocząć odliczanie do wyświetlenia alfabetu.")

tytul['font'] = myFont1
instrukcja['font'] = myFont2

b1 = Button(window, text = "Rozpocznij", command = b1_akcja)
b2 = Button(window, text = "Wyjdź", command = b2_akcja)

b1['font'] = myFont2
b2['font'] = myFont2

tytul.pack()
instrukcja.pack()
b1.pack()
b2.pack()

window.mainloop()
