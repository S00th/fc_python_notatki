####### Operacje arytmetyczne
# Są to podstawowe działania matematyczne wykonywane na danych liczbowych takich jak int i float za pomocą  symboli zwanych operatorami arytmetycznymi.
# Zawsze zwracają wartość numeryczną.

a, b = 10, 3

# Operatory arytmetyczne:

print('dodawanie: ', a + b) # Dodawanie
print('odejmowanie: ', a - b) # Odejmowanie
print('mnożenie: ', a * b) # Mnożenie
print('dzielenie: ', a / b) # Dzielenie. Zawsze zwraca float (liczbę zmiennoprzecinkową)
print('potęgowanie: ', a ** b) # Potęgowanie (a do potęgi b) przy pomocy operatora
#lub
print('potęgowanie: ', pow(a, b)) # Potęgowanie (a do potęgi b) przy pomocy wbudowanej FUNKCJI. Nie używamy, ponieważ mamy operator
print('pierwiastkowanie: ', a ** (1/b)) # Pierwiastkowanie (pierwiastek 3 stopnia z 10)

print('dzielenie: ', a / b) # Dzielenie. Zawsze zwraca float (liczbę zmiennoprzecinkową)
print('dzielenie całkowite: ', a // b) # Dzielenie całkowite. Dla 10 // 3 da wynik 3, bo w 10 mieszczą się 3 trójki i reszta 1
print('dzielenie modulo: ', a % b) # Dzielenie module: Reszta z dzielenia. Przydatne podczas sprawdzania parzystości liczby: print(a % 2 == 0)

print('Iloczyn skalarny: ', a @ b) # Iloczyn skalarny. Warto zapamiętać planując pracę przy sieciach neuronowych


### ĆWICZENIE – Czy liczba jest parzysta?

a = int(input('Podaj liczbę: '))
print(a % 2 == 0)

# if a % 2:
#     print('Liczba jest nieparzysta')
# else:
#     print('Liczba jest parzysta')

