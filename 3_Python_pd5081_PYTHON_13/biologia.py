from collections import Counter


def opis_komorki():
    return "Komórka to podstawowa forma życia."

def licz_nukleotydy(sekwencja):
    sekwencja = sekwencja.upper() 
    licznik_nukleotydow = Counter(sekwencja)
    return licznik_nukleotydow
