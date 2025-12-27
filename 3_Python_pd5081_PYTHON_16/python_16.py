import pandas as pd
import numpy as np
import matplotlib.pyplot  as plt
import seaborn as sns


geny = ['GenA', 'GenB', 'GenC']
proby = ['Proba1', 'Proba2', 'Proba3']
ekspresja = np.array([
        [5.1, 2.3, 7.8], # Ekspresja GenA
        [3.2, 4.5, 6.1], # Ekspresja GenB
        [4.8, 5.5, 3.9] # Ekspresja GenC
        ])

# Pierwszy wykres
plt.figure(figsize=(5, 5))

for i, gen in enumerate(geny):
    plt.plot(proby, ekspresja[i], marker='o', label=gen)

plt.title('Wykres liniowy ekspresji genów w próbkach')
plt.xlabel('Próbki')
plt.ylabel('Ekspresja')
plt.legend(title="Geny")

# Zapis do pliku
plt.savefig('ekspresja_genów.png', dpi=100)

# Drugi wykres
plt.figure(figsize=(5, 5))
width = 0.2 
x = np.arange(len(proby))
for i, gen in enumerate(geny):
    plt.bar(x + i * width, ekspresja[i], width, label=gen)
plt.xticks(x + width, proby)
plt.title('Wykres słupkowy ekspresji genów w próbkach')
plt.xlabel('Próbki')
plt.ylabel('Ekspresja')
plt.legend(title="Geny")


# Wycięcie wartości ekspresji
ekspresje_genA = (ekspresja[0].tolist())
ekspresje_genB = (ekspresja[1].tolist())
ekspresje_genA_genB = ekspresje_genA + ekspresje_genB

dane = {
    'Gen' : ['GenA', 'GenA', 'GenA', 'GenB', 'GenB', 'GenB'],
    'Próbka': proby*2,
    'Ekspresja': ekspresje_genA_genB
}
dane = pd.DataFrame(dane)

# Trzeci wykres
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Próbka', y='Ekspresja', hue='Gen', data=dane)
plt.title('Wykres rozrzutu ekspresji')


