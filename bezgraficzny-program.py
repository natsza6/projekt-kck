import time
alphabet = "aąbcćdeęfghijklłmnńoóprsśtuwzżź"

print("Ile liter ma Twoje słowo?")
dlugosc=int(input())

print("Rozpocznie się zaraz odliczenie do wyświetlenia alfabetu.")
time.sleep(1)
for i in range(3,0,-1):
    print(i)
    time.sleep(1)

for i in range(dlugosc):
    for litera in alphabet:
        print(litera)
        time.sleep(3)
        print("przerwa")
        time.sleep(3)
