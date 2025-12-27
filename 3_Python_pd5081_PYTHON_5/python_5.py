import random

sekwencja_dna_str = str("TCCCAAGATATG")
print("Nasza sekwencja: ", sekwencja_dna_str, ", jest typu: ", type(sekwencja_dna_str))

sekwencja_dna_list = list(sekwencja_dna_str)
print("Nasza sekwencja: ", sekwencja_dna_list, ", jest typu: ", type(sekwencja_dna_list))


# Sztuczne Generowanie Sekwencji
dlugosc_sekwencji = 10
nukleotydy = ['A', 'T', 'C', 'G']
sekwencja_sztuczna = ""
for i in range(0,dlugosc_sekwencji):
    x = int(random.randrange(4))
    sekwencja_sztuczna += nukleotydy[x]

print("Sztucnza sekwencja: " + sekwencja_sztuczna)