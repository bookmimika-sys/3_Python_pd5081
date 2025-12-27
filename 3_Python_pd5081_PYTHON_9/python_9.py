# Utwórz zbiór i słownik
sekwencje_genowe = {"CCTGA", "ATAGC", "TTTGA"}

geny = {
"BRCA1": "naprawa DNA",
"EGFR": "sygnalizacja wzrostu"
}

# Dodaj wartości
sekwencje_genowe.add("GTGTG")
geny["TP53"] = "regulacja cyklu komórkowego"

# Sprawdz czy istnieje w zbiorze
print("Czy sekwencja w zbiorze: ", ("CCCCC" in sekwencje_genowe), "\nCzy gen w słowniku: ", ("TP53" in geny))

# Usuwanie ze zbioru
sekwencje_genowe.remove("ATAGC")
print(sekwencje_genowe)

# Pętla for dla wyświetlenia zawartości słownika
for klucz, wartosc in geny.items():
    print(f"{klucz}: {wartosc}")

if len(sekwencje_genowe) >= 3:
    print("Sekwencja genowa zawiera 3 lub więcej elementów")
else:
    print("Sekwencja genowa zawiera mniej od 3 elementów")

if "TP53" in geny:
    print(geny["TP53"])

# Wnion na sekwencjach
sekwencje_genowe_2 = {"CAT", "GTAAA"}
union_sekwencji = sekwencje_genowe.union(sekwencje_genowe_2)

print(union_sekwencji)
