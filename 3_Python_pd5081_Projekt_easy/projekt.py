from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Nazwa pliku
file_name = 'sekwencje.fasta'


# Sprawdz czy sekwencja jest dobra
def sprawdz_sekwencje_dna(sekwencja)->bool:
    dozwolone_nukleotydy = set('ATCG')
    if not set(sekwencja.upper()).issubset(dozwolone_nukleotydy):
        return False
    return True


# Odczyt z pliku
try:
    sekwencje = list(SeqIO.parse(file_name, "fasta"))
except FileNotFoundError:
    print("Nie znaleziono pliku z sekwencjami.")


# Dodawanie własnej sekwencji w formacie Fasta
wlasna_nazwa = input("Podaj id/nazwę własnej sekwencji: ")
wlasna_sekwencja = None


# Prosi o prawidłową sekwencje do skutku
while not wlasna_sekwencja:
    wlasna_sekwencja = input("Podaj własną sekwencje: ")
    if not sprawdz_sekwencje_dna(wlasna_sekwencja):
        wlasna_sekwencja = None


# Tworzenie nowego rekurdu typu Bio.SeqRecord.SeqRecord
nowa_sekwencja = SeqRecord(id = wlasna_nazwa, seq=Seq(wlasna_sekwencja))


# Dodanie sekwencji do naszej listy
sekwencje.append(nowa_sekwencja)


# Dodanie sekwencji do pliku
with open(file_name, "a") as out_f:
    SeqIO.write(nowa_sekwencja, out_f, "fasta")


# Wyświetl sekwencje i jej dane
for sekwencja in sekwencje:
    ilosc_gc = str(sekwencja.seq).upper().count('GC')
    ilosc_t = str(sekwencja.seq).upper().count('T')
    ilosc_g = str(sekwencja.seq).upper().count('G')
    ilosc_c = str(sekwencja.seq).upper().count('C')
    ilosc_a = str(sekwencja.seq).upper().count('A')
    dlugosc_sekwencji = len(str(sekwencja.seq))
    prawidlowa_sekwencja = sprawdz_sekwencje_dna(str(sekwencja.seq))
    print(f"Sekwencja o nazwie = {sekwencja.name}, opis sekwencji: {sekwencja.description}\nSekwencja prawidłowa: {prawidlowa_sekwencja}\nDługość sekwencji: {dlugosc_sekwencji}\nIlość GC: {ilosc_gc}, ilość A: {ilosc_a}, ilość C: {ilosc_c}, ilość T: {ilosc_t}, ilość G: {ilosc_g}")
    

# Utwórz słownik z listy (jako że słowniki są unikatowe duplikaty usuną się same)
klucze_do_slownika = [sekwencja.id for sekwencja in sekwencje]
sekwencje_do_slownika = [sekwencja for sekwencja in sekwencje]
sekwencje_slownik = dict(zip(klucze_do_slownika, sekwencje_do_slownika))


# Uworz Dataframe ze slownika
sekwencje_df = pd.DataFrame(sekwencje_slownik.items(), columns=['id', 'sekwencja_obiekt'])
sekwencje_df['opis'] = [sekwencja.description for sekwencja in sekwencje_df["sekwencja_obiekt"]]
sekwencje_df['organizm'] = [(opis.split(' ')[1]) + " " + (opis.split(' ')[2]) if '<unknown description>' not in opis else 'Unidentfied' for opis in sekwencje_df["opis"]]
sekwencje_df['sekwencja'] = [str(sekwencja.seq) for sekwencja in sekwencje_df["sekwencja_obiekt"]]
sekwencje_df['dlugosc'] = sekwencje_df['sekwencja'].str.len()


# Usuwanie wadliwych sekwencji
sekwencje_df = sekwencje_df[
    sekwencje_df['sekwencja'].apply(sprawdz_sekwencje_dna)]
print(sekwencje_df)


# Wizualizacje 

# Pierwsza wizualizacja - dla 5 najczęściej występujących organizmów
top_organizmy = sekwencje_df['organizm'].value_counts().head(5)

plt.figure(figsize=(12, 6))
plt.barh(top_organizmy.index, top_organizmy.values)
plt.xlabel('Liczba sekwencji')
plt.ylabel('Organizm')
plt.title('Top 5 organizmów a liczba sekwencji')
plt.show()


# Druga wizualizacja - częstość występowania A C T G we wszystkich dostępnych sekwencjach
zlaczone_sekwencje = ''.join(sekwencje_df['sekwencja'].str.upper())
licznik = Counter(zlaczone_sekwencje)

plt.bar(licznik.keys(), licznik.values())
plt.xlabel('Nukleotyd')
plt.ylabel('Liczba wystąpień')
plt.title('Nukleotydy w sekwencjach')
plt.show()


# Trzecia wizualizacja - długość genów 
plt.hist(sekwencje_df['dlugosc'], bins=30)
plt.xlabel('Długość sekwencji')
plt.ylabel('Liczba sekwencji')
plt.title('Rozkład długości sekwencji DNA')
plt.show()


# Czwarta wizualizacja - średnia długość genów na organizm
srednia_dlugosc = (
    sekwencje_df
    .groupby('organizm')['dlugosc']
    .mean()
    .sort_values(ascending=False)
    .head(5)
)
print(type(srednia_dlugosc))

plt.figure(figsize=(15, 5))
plt.scatter(srednia_dlugosc.index, srednia_dlugosc.values)
plt.xlabel('Organizm')
plt.ylabel('Średnia długość genu')
plt.title('Średnia długość genów a organizm')
plt.tight_layout()
plt.show()