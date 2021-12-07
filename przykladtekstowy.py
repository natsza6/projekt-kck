
import tkinter as tk
import time
import random
from tkinter import messagebox
from tkinter import *
import tkinter.font as font
import string
from string import ascii_uppercase

class mruganie(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.label = tk.Label(self, width='700', height = '1000')
        self.label.pack()
        self.remaining = 0
        self.myFont3 = font.Font(family='arial', size=350, weight='bold')
        self.countdown(4)
        self.allletters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


    def countdown(self, remaining = None):

        if remaining is not None:
            self.remaining = remaining
            self.label.configure(font = self.myFont3)

        if self.remaining <= 0:
            self.label.configure(text=" ")
            self.letter()
        else:
            self.label.configure(text="%d" % self.remaining)
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)


    def letter(self):

                for i in ascii_uppercase:
                    self.label.configure(text = i, font = self.myFont3)
                    #self.label.configure(text = self.oneletter, font = self.myFont3)
                    #time.sleep(2)
                    #self.letter()

if __name__ == "__main__":
    app = mruganie()
    app.mainloop()
