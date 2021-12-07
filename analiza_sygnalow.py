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

    # wszystkie funkcje
    def make_widget(widget):
        widget.pack()
    def destroy_wiget(widget):
        widget.destroy()

    def odliczanie_label(label):
        global counter
        counter = 4
        def count():
            global counter
            counter -= 1
            if counter <= 0:
                counter = 0
                odliczanie_liczby.destroy()
                return

            label.config(text=str(counter))
            label.after(1000,count)
        count()
        
    def letter():
        alfabet = "AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWZŻŹ"
        alfabet_label = tk.Label(window,width='700', height = '1000')
        alfabet_label.pack()
        for i in alfabet:
            oneletter = i
            alfabet_label.configure(text = oneletter, font = myFont3)
            window.after(3000,letter)

    tytul_odliczanie = tk.Label(window, text = "Do wyświetlenia pierwszej litery alfabetu pozostało:")
    tytul_odliczanie['font'] = myFont2
    tytul_odliczanie.pack()
    window.after(3000, destroy_wiget,tytul_odliczanie)

    odliczanie_liczby = tk.Label(window)
    odliczanie_liczby['font'] = myFont3
    odliczanie_liczby.pack()
    odliczanie_label(odliczanie_liczby)
    
    window.after(3000,letter)

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
