####### Operacje porównania
# Służą do zestawiania ze sobą dwóch wartości w celu określenia relacji między nimi.
# Zawsze zwracają wartość logiczną bool (Boolean), czyli zmienną logiczną True (prawda) lub False (fałsz).

a = 10
b = 5

# Operatory porównania:

print(a == b) # Zwraca True, jeśli obie wartości są IDENTYCZNE
print(a != b) # Zwraca True, jeśli obie wartości są RÓŻNE
# Użycie: == != między różnymi typami danych zwróci False, ponieważ LICZBA nie może być identyczna z TEKSTEM.

print(a > b) # Zwraca True, jeśli lewa wartość jest WIĘKSZA od prawej
print(a >= b) # Zwraca True, gdy lewa wartość jest WIĘKSZA lub równa prawej
print(a < b) # Zwraca True, jeśli lewa wartość jest MNIEJSZA od prawej
print(a <= b) # Zwraca True, gdy lewa wartość jest MNIEJSZA lub równa prawej
# Użycie: > < >= <= między różnymi typami zmiennych wywoła TypeError

print('adam' == 'Adam') # False – ponieważ wielkość liter ma znaczenie