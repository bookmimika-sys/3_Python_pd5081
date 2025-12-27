# funkcja charakterystyka białka
def charakterystyka_białka(sekwencja_bialka, masa, pI):
    return f"Sekwencja białka: {sekwencja_bialka} o masie {masa} i punkcie izoterycznym {pI}."

# funkcja sumująca cechy białek
def sumuj_cechy_bialek(**cechy):
    suma_mas = 0
    suma_pI = 0
    ilosc_pI = 0
    for klucz, wartosc in cechy.items():
        if 'masa' in klucz:
            suma_mas += wartosc
        if 'pI' in klucz:
            suma_pI += wartosc
            ilosc_pI += 1

    return suma_mas, (suma_pI/ilosc_pI)

print(charakterystyka_białka("AGGTC",2.2,1.4))

print(sumuj_cechy_bialek(
    masa_1=3.3,
    masa_2=2.3,
    pI_1=6.8,
    pI_2=1.5
))
    
 