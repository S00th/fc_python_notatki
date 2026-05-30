####### OPERATORY PORÓWNANIA

# OPERATORY PORÓWNANIA (comparison Operators) służą do sprawdzania RELACJI między dwiema WARTOŚCIAMI (np. LICZBAMI lub TEKSTAMI).
# Zawsze zwracają wartość logiczną bool (boolean), czyli ZMIENNA LOGICZNĄ True (prawda) lub False (fałsz).
# Wynikiem porównania ZMIENNYCH jest zawsze WARTOŚĆ typu bool.

a = 10
b = 5

# OPERATORY PORÓWNANIA

print(a == b) # Zwraca True, jeżeli obie wartości są IDENTYCZNE
print(a != b) # Zwraca True, jeżeli obie wartości są RÓŻNE
# Użycie: == != między RÓŻNYMI TYPAMI DANYCH zwróci False, ponieważ LICZBA nie może być identyczna z TEKSTEM.

print(a > b) # Zwraca True, jeżeli lewa wartość jest WIĘKSZA od prawej
print(a >= b) # Zwraca True, jeżeli lewa wartość jest WIĘKSZA lub równa prawej
print(a < b) # Zwraca True, jeżeli lewa wartość jest MNIEJSZA od prawej
print(a <= b) # Zwraca True, jeżeli lewa wartość jest MNIEJSZA lub równa prawej
# UWAGA! Użycie OPERATORÓW PORÓWNANIA między różnymi TYPAMI ZMIENNYCH wywoła TypeError.
# Przykład 123 <= Adam

print('adam' == 'Adam') # False – ponieważ wielkość liter ma znaczenie