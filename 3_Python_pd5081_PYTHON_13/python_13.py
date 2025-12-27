import os
import biologia
import datetime

print(biologia.opis_komorki())

# Nowy folder i nadpisanie wyniku funkcji
nowy_katalog = "dane_bio"
if not os.path.exists(nowy_katalog):
    os.mkdir(nowy_katalog)
sekwencja = 'AGCTTAGCTAAGGCT'

with open(nowy_katalog + "\\nukleotydy.txt", "w") as plik:
    plik.write(str(biologia.licz_nukleotydy(sekwencja)))
    print("Wpisano liczbe nukleotydów")

# Dodanie daty i czasu 
czas_teraz = datetime.datetime.now()

with open(nowy_katalog + "\\nukleotydy.txt", "a") as plik:
    plik.write('\n' + str(czas_teraz))
    print("Wpisano date i czas")