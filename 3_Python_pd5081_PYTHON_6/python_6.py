import random

# Sztuczne Generowanie 2 Sekwencji
dlugosc_sekwencji = 10
nukleotydy = ['A', 'T', 'C', 'G']
sekwencja_dna1 = ""
sekwencja_dna2 = ""

for i in range(0,dlugosc_sekwencji):
    x = int(random.randrange(4))
    sekwencja_dna1 += nukleotydy[x]
    x = int(random.randrange(4))
    sekwencja_dna2 += nukleotydy[x]

sekwencja_dna_polaczona = sekwencja_dna1 + sekwencja_dna2
print("Połączona sekwencja: ", sekwencja_dna_polaczona) 

wycieta_sekwencja = print(sekwencja_dna_polaczona[3:12]) 
print("Wycięta sekwencja: ", wycieta_sekwencja)

# Zamień "T" na "G"
zamieniona_sekwecja = sekwencja_dna_polaczona.replace("T", "G")
print("Zamieniona sekwencja: ", zamieniona_sekwecja)

# Wylicz "T"
ilosc_T = zamieniona_sekwecja.count("G")
print("Ilość T w sekwencji zamienionej: ", ilosc_T)

opis = f"Zamieniona sekwencja: {zamieniona_sekwecja}"

print(f"{opis} \nDodatkowo zawiera {ilosc_T} T")
