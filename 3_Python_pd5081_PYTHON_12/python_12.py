class NieprawidłowaSekwencjaDNA(Exception):
    def __init__(self, sekwencja, wiadomość="Sekwencja zawiera nieprawidłowe nukleotydy"):
        self.sekwencja = sekwencja
        self.wiadomość = wiadomość
        super().__init__(self.wiadomość)

try:
    plik = open("sekwencje.txt", "r")
    sekwencja_dna = plik.read()
except FileNotFoundError:
    print("Plik nie istnieje.")


wlasna_sekwencja = str(input("Podaj swoją sekwencje"))

dozwolone_nukleotydy = set('ATCG')
if not set(wlasna_sekwencja.upper()).issubset(dozwolone_nukleotydy):
    raise NieprawidłowaSekwencjaDNA(wlasna_sekwencja)

    
try:
    plik = open("sekwencje.txt", "w")
    sekwencja_dna = plik.write(wlasna_sekwencja)
finally:
    plik.close()
    print("Plik został zamknięty.")
