import pandas as pd
import matplotlib.pyplot as plt
import aseegg as ag 
import numpy as np
import random

import pandas as pd

#import i wyświetlenie zebranych danych
dane_nasze = pd.read_csv('dane.txt',delimiter="\t", names=['Sygnal'])
dane_nasze[['Sygnal','Czas']] = dane_nasze.Sygnal.str.split(",",expand=True,)

dane_nasze

#podstawowy, pierwotny wykres

t = np.linspace(0,len(dane_nasze)/200,len(dane_nasze))

dane1 = dane_nasze['Sygnal'].astype(float)

plt.plot(t,dane1)
plt.xlabel('Czas [s]')
plt.ylabel('Amplituda [uV]')
plt.show()

#filtracja sygnału

przef = ag.gornoprzepustowy(dane1,200,0.1)
przef2 = ag.pasmowozaporowy(przef,200,45,55)
przef3 = ag.pasmowoprzepustowy(przef2,200,1,40) 

przef3

#wykres po filtracji

plt.plot(t,przef3)
plt.xlabel('Czas [s]')
plt.ylabel('Amplituda [uV]')
plt.show()

#wykres zawężony do potencjałów słowa
plt.plot(przef3[3800:11000])
plt.xlabel('indeks sygnału')
plt.ylabel('Amplituda [uV]')
plt.show()

#zamiana mrugnięć na wartości "0" (brak) i "1" (akcja)

blinks = []
for value in przef3:
    if value < -40000:
        blinks.append('1')
    else:
        blinks.append('0')
        
print(blinks)

#wykres wymrugania słowa dla sygnałów == 0 bądź 1

plt.plot(blinks[3800:11600])
plt.show()

#wyszukiwanie początków mrugnięć

blinks_word = blinks[3800:11700]

blinks_word

poczatki_zdarzen = []
for i in range(len(blinks_word)):
    if blinks_word[i]=='1' and blinks_word[i-1]=='0':
        poczatki_zdarzen.append(i)
    
poczatki_zdarzen

#1. próba odczytania słowa

poczatki_zdarzen=[574+800,1885+800,3886+800,5560+800,7770+800]
Alfabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
for i in range(5):
    Alfabet+=Alfabet
wektor=[]
wyraz=''
for i in range(len(Alfabet)):
    wektor.append(100*i)
    
for i in range(len(poczatki_zdarzen)):
    for j in range(len(wektor)):
        if poczatki_zdarzen[i]>=wektor[j] and poczatki_zdarzen[i]<wektor[j+1]:
            wyraz+=Alfabet[j]
        
wyraz

#wyszukiwanie niewykrytego wcześniej "A"
plt.plot(blinks[11500:11600])
plt.show()

#przybliżenie wyszukiwania wyżej
plt.plot(blinks[11550:11600])
plt.show()

#odczytanie przybliżone = 6974

#próba 2. odczytania słowa

poczatki_zdarzen=[574+800,1885+800,3886+800,5560+800,6974+800]
Alfabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
for i in range(5):
    Alfabet+=Alfabet
wektor=[]
wyraz=''
for i in range(len(Alfabet)):
    wektor.append(100*i)
    
for i in range(len(poczatki_zdarzen)):
    for j in range(len(wektor)):
        if poczatki_zdarzen[i]>=wektor[j] and poczatki_zdarzen[i]<wektor[j+1]:
            wyraz+=Alfabet[j]
        
wyraz

#słowo mrugane: NAULA (pierwotnie NAURA, R->L w trakcie - błąd ludzki)

#"Z" chwilę przed "A"; ze względu na zapętlenie alfabetu
#uznajemy przedwczesne mrugnięcie za błąd ludzki
