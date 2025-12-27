sekwencja_dna = ['A', 'T', 'G', 'C', 'A', 'T', 'G', 'G']
zasady_azotowe = ('Adenina', 'Tymina', 'Cytozyna', 'Guanina')

pierwsza_zasada = zasady_azotowe[0] 
ostatnia_zasada = zasady_azotowe[-1] 

sekwencja_dna[5] = "A"

#zasady_azotowe[3] = "Cytozyna"

sekwencja_dna.append("C")

print(sekwencja_dna)

for i in sekwencja_dna:
    print(i)

for i in zasady_azotowe:
    print(i)

sekwencja_dna_bez_T = [n for n in sekwencja_dna if n != "T"]

print(sekwencja_dna_bez_T)

