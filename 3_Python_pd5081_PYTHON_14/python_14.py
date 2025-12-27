import numpy

macierz_ekspresji = numpy.array([[1.8, 6.4, 3.1],
                              [9.2, 0.7, 4.9],
                              [5.6, 2.3, 8.8],
                              [7.1, 3.9, 0.4]])


# Zwiększenie ekspresji
skorygowana_ekspresja = macierz_ekspresji * 1.05

print(skorygowana_ekspresja)

# Średnia ekspresji
srednia_ekspresji = numpy.mean(skorygowana_ekspresja, axis=1)

print(srednia_ekspresji)

# Oblicz sume ekspresji
suma_ekspresji = numpy.sum(skorygowana_ekspresja, axis=0)

print(suma_ekspresji)

# Obsługa brakujących danych - wprowadzenie nan
skorygowana_ekspresja[1, 0] = numpy.nan
skorygowana_ekspresja[0, 2] = numpy.nan
skorygowana_ekspresja[3, 1] = numpy.nan

#print(skorygowana_ekspresja)

# Średnia ekspresji znan
srednia_ekspresji_nan = numpy.nanmean(skorygowana_ekspresja, axis=1)

print(srednia_ekspresji_nan)



