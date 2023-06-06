import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from  PIL import Image

#zad1
x = np.linspace(-5, 5, 13)
y = x**2 + np.sin(x)
plt.plot(x, y, label='f(x) = x^2 + sin(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Wykres funkcji f(x) = x^2+sin(x)')
plt.legend()
plt.xlim([-5, 5])
plt.savefig('Piotr_Sitkowski_zad1.png')
plt.show()

#zad2
x1 = np.arange(-2, 2.1, 0.1)
x2 = np.arange(-3, 3.1, 0.1)
y1 = np.tan(x1)*np.sin(x1)
y2 = np.sin(x2)+np.tan(x2)

plt.subplot(2, 2, 2)
plt.plot(x1, y1, 'g--', label='tan(x)*sin(x)')
plt.title('Pierwszy wykres')
plt.xlabel('x')
plt.ylabel('wynik funkcji')
plt.legend()
plt.axis([-2, 2, -40, 20])
plt.show()

plt.subplot(2, 2, 3)
plt.plot(x2, y2, 'lightblue', label='sin(x)+tan(x)')
plt.title('Drugi wykres')
plt.xlabel('x')
plt.ylabel('wynik funkcji')
plt.legend()
plt.axis([-3, 3, -40, 40])
plt.xlim(-3, 3)
plt.subplots_adjust(hspace=0.5)
plt.savefig('Piotr_Sitkowski_zad2.png')
plt.show()

#zad3
df = pd.read_csv('wine.data', header=None)
print(df)
# Wyświetlanie wiersza o etykiecie 0
# wiersz = df.loc[0]
# print(wiersz)
# df[4] = pd.to_numeric(df[5], errors='coerce')
klasy = df[df[0].isin(['1', '2'])]
print(klasy)
# pogrupowane = klasy.groupby(0)
# print(pogrupowane)
srednia_magnezu = klasy.groupby(0)[5].mean()
print(srednia_magnezu)
srednia_magnezu.plot(kind='bar', rot=0)
plt.xlabel('Klasy')
plt.ylabel('Srednia Magnezu')
plt.title('Srednia Magnezu dla klas win')
plt.savefig('Piotr_Sitkowski_zad3.png')
plt.show()

#zad4
df = pd.read_csv('wine.data', header=None, skiprows=1)
print(df)
grupowanie = df.groupby(0).size()
print(grupowanie)
fig, ax = plt.subplots()
ax.pie(grupowanie, labels=grupowanie.index, autopct='%.2f%%', textprops={'fontsize': 14})
ax.set_title('Procentowy udział klas w zbiorze win')
ax.legend(title='Klasy')
plt.savefig('Piotr_Sitkowski_zad4.png')
plt.show()