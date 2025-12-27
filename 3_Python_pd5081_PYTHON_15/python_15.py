import pandas
import numpy as np

dane = {
    'Gen': ['GenA', 'GenB', 'GenC', 'GenD'],
    'Proba1': [5.1, 2.3, np.nan, 4.4],
    'Proba2': [3.2, 4.5, 3.9, np.nan],
    'Proba3': [6.3, 5.6, np.nan, 6.6]
    }

# Sprawdz nulle
dane = pandas.DataFrame(dane)
print(dane.isnull())

# Usuń nulle
dane_bez_nan = dane.dropna()
print(dane_bez_nan)

# Uzupełnij przez wypełnienie średnią
dane_uzupelnione = dane.fillna(dane[['Proba1', 'Proba2', 'Proba3']].mean())
print(dane_uzupelnione)

# Wyciągnięcie danych dla GenA
genA = dane_uzupelnione[dane['Gen'] == 'GenA']
print(f"Dane genu GenA:\n{genA}")

# Średnia dla próbek
srednia_ekspresja = dane_uzupelnione[['Proba1', 'Proba2', 'Proba3']].mean()
print(srednia_ekspresja)

# Ekspresja powyżej > 4
ekspresja_powyzej_4 = dane_uzupelnione[dane_uzupelnione['Proba1'] > 4]
print("Geny o ekspresji powyzej 4 w próbce 1:\n", ekspresja_powyzej_4)

# Zapisz wyniki
dane_uzupelnione.to_csv("wyniki.csv")

