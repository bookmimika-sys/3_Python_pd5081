# Parametr wagi
waga = 65.5

# Parametr wzrostu
wzrost = 165

print("Waga wynosi ", waga, " i jest typu ", type(waga), "\nWzrost wynosi ", wzrost, " i jest typu ", type(wzrost))

#oblicznie BMI
bmi = waga / ( (wzrost/100) * (wzrost/100) )

print("BMI wynosi ", bmi)