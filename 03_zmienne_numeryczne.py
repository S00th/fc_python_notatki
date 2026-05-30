####### Zmienne NUMERYCZNE

### INTEGERS (int): Liczby całkowite, np. 2 lub -2. Liczby całkowite mogą być dowolnie duże (lub małe) i mogą przyjmować wartości ujemne.

x = 3 # Można przypisać kilka liczby do kilku ZMIENNYCH jak tutaj – czyli każda zmienna w oddzielnej linii
y = 30
z = 10
# lub
a, b, c = 6, 60, 10 # Można przypisać kilka liczb do kilku ZMIENNYCH jednej linii.

print(type(2)) # Sprawdź typ danych
print(type(-2))
print(type(2.5))
print(type('dwa'))
print(type(True))

# POWIADOMIENIA TYPÓW – (type annotation / type hinting)
height1: int = 180 # Python sam rozpoznaje typy danych, ale można mu je podpowiedzieć
height2 = 'napis'

# SEPARATOR DZIESIĘTNY
# W Pythonie separatorem dziesiętnym jest KROPKA.
data = 1.5 # Prawidłowy zapis liczby 1.5 w Pythonie (z KROPKĄ).
data2 = 1,5 # Zapis z PRZECINKIEM spowoduje, że Python nie zauważy liczby 1.5, a ZBIÓR DANYCH (tuple) składającą się z 1 i 5.
print(type(data), type(data2)) # W pierwszym przypadku dowiemy się, że jets to typ float, w drugim tuple

# SEPARATOR WIZUALNY – Separator tysięczny
miliard_v1 = 1_000_000_000 # Aby ułatwić sobie odczyt wielkich liczb, możemy użyć separatora wizualnego _
print(miliard_v1)
miliard_v2 = 1000000000 # PYTHON nie widzi różnicy między zapisem wyżej o tym obok.
print(miliard_v2)

# ZAOKRĄGLENIE (rounding)
pi = 3.14159265359
print(round(pi, 3))
print(round(pi))

# INTEGER vs ROUNDING – Czym się różnią?
num = 3.89
print(int(num)) # Integer NIE ZAOKRĄGLA, po prostu UCINA WARTOŚĆ po przecinku.
print(round(num)) # round() zaokrągla w górę lub w dół (do bliższej wartości) UWAGA! num = 3.50 to 4.

# F-STRING ROUNDING – Kolejny sposób zaokrąglania
print(f'PI 2 decimal places {pi:.4f}') # Nowoczesnym i bardzo czytelnym sposobem łączenia tekstów ze zmiennymi,
# która automatycznie dba o konwersję typów i jest uważany za styl Pythonic.



print('####### ####### ####### ĆWICZENIE – Cena brutto ####### ####### #######')
print()

# Mamy kilka produktów i chcemy obliczyć ich cenę brutto przy zadanej stawce podatku.

tax_rate = 0.23
item1_netto_price = 100
item2_netto_price = 345
item3_netto_price = 30.50

print('Produkt 1:', item1_netto_price, 'zł (cena netto)')
print('Produkt 2:', item2_netto_price, 'zł (cena netto)')
print('Produkt 3:', item3_netto_price, 'zł (cena netto)')
print()

print('Produkt 1:', item1_netto_price + (item1_netto_price * tax_rate), 'zł (cena brutto)')
print('Produkt 2:', item2_netto_price + (item2_netto_price * tax_rate), 'zł (cena brutto)')
print('Produkt 3:', item3_netto_price + (item3_netto_price * tax_rate), 'zł (cena brutto)')
print()
# lub
print('Produkt 1:', 100 + (100 * 0.23), 'zł (cena brutto)')
print('Produkt 2:', 345 + (345 * 0.23), 'zł (cena brutto)')
print('Produkt 3:', 30.50 + (30.50 * 0.23), 'zł (cena brutto)')
print()
