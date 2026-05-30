####### OPERACJE ARYTMETYCZNE

# OPERACJE ARYTMETYCZNE to podstawowe działania matematyczne wykonywane na danych liczbowych takich jak int i float.
# Operacje arytmetyczne wykonywane są za pomocą symboli zwanych OPERATORAMI ARYTMETYCZNYMI.
# OPERACJE ARYTMETYCZNE zawsze zwracają wartość numeryczną.

## OPERATORY ARYTMETYCZNE

a, b = 10, 3

print('dodawanie: ', a + b) # Dodawanie.
print('odejmowanie: ', a - b) # Odejmowanie.
print('mnożenie: ', a * b) # Mnożenie.
print('potęgowanie: ', a ** b) # Potęgowanie (a do potęgi b).
# lub
# print('potęgowanie: ', pow(a, b)) # Potęgowanie (a do potęgi b) przy pomocy wbudowanej FUNKCJI. NIE UŻYWAMY, ponieważ mamy operator **.

print('pierwiastkowanie: ', a ** (1/b)) # Pierwiastkowanie (pierwiastek 3 stopnia z 10)

print('dzielenie: ', a / b) # Dzielenie ZWYKŁE – Zwraca PEŁNY WYNIK wraz z częścią, po przecinku (ułamkiem) – zawsze typ float.
print('dzielenie całkowite: ', a // b) # Dzielenie CAŁKOWITE – Zwraca tylko część CAŁKOWITĄ wyniku, "ucina" część po przecinku – zawsze typ int.
print(10 // 3) # Wyświetli wynik 3, ponieważ w 10 mieszczą się trzy 3 i reszta 1, ale reszta zostaje "ucięta".

print('dzielenie modulo: ', a % b) # Dzielenie MODULO – Zwraca WYŁĄCZNIE RESZTĘ, która została po wykonaniu dzielenia całkowitego – zawsze typ int.
print(10 % 2) # Wyświetli 0, ponieważ 2 jest podzielna przez 2 (NIE MA wartości po przecinku).
print(10 % 3) # Wyświetli 1, ponieważ 3 nie jest podzielna przez 2 (MA wartość po przecinku).
print(10 % 2 == 0) # Wyświetli True
print(10 % 3 == 0) # Wyświetli False
print(10 % 2 == 1) # Wyświetli False
print(10 % 3 == 1) # Wyświetli True

print('Iloczyn skalarny: ', a @ b) # Iloczyn skalarny. Warto zapamiętać planując pracę przy sieciach neuronowych

print(10 / 2) # Wyświetli 5.0
print(10 // 2) # Wyświetli 5
print(10 % 2) # Wyświetli 0
print()
print(10 / 3) # Wyświetli 3.3333333333333335
print(10 // 3) # Wyświetli 3
print(10 % 3) # Wyświetli 1



print('####### ####### ####### ĆWICZENIE – Czy liczba jest parzysta? ####### ####### #######')
print()

# Sprawdź, czy podana przez użytkownika liczba jest parzysta?

number = int(input('Podaj liczbę: '))

if number % 2 == 0: # WARUNEK mówi: Jeżeli LICZBA podzielona przez 2 NIE MA reszty z dzielenia (reszta wynosi 0), to będzie to PRAWDA.
    print('Liczba jest parzysta')
else:
    print('Liczba jest nieparzysta')

