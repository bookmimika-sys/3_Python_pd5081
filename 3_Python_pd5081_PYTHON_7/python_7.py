import random

# Sztuczne Generowanie Sekwencji
dlugosc_sekwencji = 200
nukleotydy = ['A', 'T', 'C', 'G']
pusta_lista = []
sekwencja_dna = ""

for i in range(0,dlugosc_sekwencji):
    x = int(random.randrange(4))
    sekwencja_dna += nukleotydy[x]

sekwencja_dna = list(sekwencja_dna)
#print(f"Nasza sekwencja: {sekwencja_dna}")


# Deklaracja zmiennych bool
czy_sekwencja_dna_aktywna = True
czy_sekwencja_zawiera_T = True if "T" in sekwencja_dna else False

print(f"Czy sekwencja DNA aktywna: {czy_sekwencja_dna_aktywna} \nCzy sekwecja DNA zawieta T: {czy_sekwencja_zawiera_T}")

print("Lista 1 zawiera elementy: " + str(bool(nukleotydy)) 
      + "\nLista 2 zawiera elementy: " + str(bool(pusta_lista))
      + "\nSekwencja zawiera elementy: " + str(bool(sekwencja_dna)))

liczba_T = sekwencja_dna.count("T")
liczba_C = sekwencja_dna.count("C")
liczba_A = sekwencja_dna.count("A")
liczba_G = sekwencja_dna.count("G")

# Operacje arytmentyczne
liczba_A_i_G = liczba_A + liczba_G
stosunek_T_do_C = liczba_T / liczba_C

print(f"Liczba A i G w sekwencji: {liczba_A_i_G} \nStosunek T do C: {stosunek_T_do_C}")

sekwencja_dna = sekwencja_dna[:4]

# Operatory przypisania i zmiana wartości
liczba_T = sekwencja_dna.count("T")
liczba_C = sekwencja_dna.count("C")
liczba_A = sekwencja_dna.count("A")
liczba_G = sekwencja_dna.count("G")

liczba_A_i_G = liczba_A
liczba_A_i_G += liczba_G

# Operatory porównania
czy_liczba_A_taka_sama_jak_C = liczba_A == liczba_C
czy_liczba_G_wieksza_od_T = liczba_G > liczba_T
print(sekwencja_dna)
print(f"Liczba T: {liczba_T} \nLiczba C: {liczba_C} \nLiczba A: {liczba_A} \nLiczba G: {liczba_G}")
print(f"Czy liczba A taka sama jak C: {czy_liczba_A_taka_sama_jak_C}, \nCzy liczba G większa od liczby T: {czy_liczba_G_wieksza_od_T}")
