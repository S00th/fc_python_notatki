####### Typy logicznie i operatory logiczne
# Typ logiczny "bool" (boolean) to wbudowany typ danych, który reprezentuje wartości logicznych.
# Przyjmuje jedną z dwóch wartości: True albo False.
# – True: reprezentuje logiczną PRAWDĘ (oznaczaną za pomocą wartości 1)
# – False: reprezentuje logiczny FAŁSZ (oznaczaną za pomocą wartości 0)
# Wartości True i False muszą być zapisane, zaczynając się od wielkiej litery.
# Wartości logiczne, są wynikiem działania operatorów porównania (czyli: ==, !=, >, <, >=, <=).
# Wartości logiczne mogą być łączone za pomocą operatorów: anr, or i not
# W przypadku, gdy porównywane są napisy, kryterium porównania jest kolejność leksykograficzna np. "a" jest mniejsze od "b"

data_true = True
data_false = False

####### Operatory logiczne
#
# and (i) – koniunkcja – Zwraca True tylko wtedy, jeżeli oba warunki są prawdziwe.
# or (lub) – alternatywa – Zwraca True, jeżeli przynajmniej jeden z warunków jest prawdziwy.
# not (nie) – negacja/zaprzeczenie – Zmienia True na False i odwrotnie (odwraca wartość logiczną warunku)

# and (i)
# Aby wejść na koncert, musisz mieć ukończone 18 lat i mieć ważny bilet.
# Jeśli zabraknie choć jednej z tych rzeczy, to otrzymamy False.
print(f'Prawda i Prawda to: {True and True}') # True
print(f'Prawda i Fałsz to: {True and False}') # False
print(f'Fałsz i Fałsz to: {False and False}') # False

# or (lub)
# Możesz wejść do budynku, jeśli masz klucz lub jeśli ktoś Cię wpuści.
print(f'Prawda lub Prawda to: {True or True}') # True
print(f'Prawda lub Fałsz to: {True or False}') # True
print(f'Fałsz lub Fałsz to: {False or False}') # False

# not (nie)
# Działa jak przełącznik światła.
print(f'Nie Prawda to: {not True}') # False
print(f'Nie Fałsz to: {not False}') # True

print(f'Nie Prawda lub Fałsz to: {not True or False}') # False lub False = False
print(f'Nie Prawda lub Fałsz to: {not True or not False}') # False lub True = True
print(f'Nie (Prawda lub Fałsz) to: {not (True or False)}') # nie (True lub False) = False



###### KONWERSJA na bool

print(bool(123)) # True
print(bool(-1)) # True
print(bool('abcd')) # True
print(bool(' '))  # True
print(bool('')) # False
print(bool(0)) # False
print(bool(0.0)) # False
print(bool(.0)) # False – 0.0 możemy zapisać także jako .0



####### Katalog zamknięty – All Negative Values
# Wymienione niżej wartości zawsze dają w Pythonie False

# 0 - ZERO integer
# 0.0 - ZERO float
# False - false BOOL
# '' - empty STRING
# () - empty TUPLE
# [] - empty LIST
# set() - empty SET
# {} - empty DICTIONARY
# None - empty or unknown value

# Wszystkie wartości w Pythonie inne niż wymienione wyżej, oznaczać będa True

a, b, c, d, e, f, g, h, i = 1, 0, -1, 0.0, None, False, True, '', ' '
print(f'bool of value {a}: {bool(a)}') # True
print(f'bool of value {b}: {bool(b)}') # False
print(f'bool of value {c}: {bool(c)}') # True
print(f'bool of value {d}: {bool(d)}') # False
print(f'bool of value {e}: {bool(e)}') # False
print(f'bool of value {f}: {bool(f)}') # False
print(f'bool of value {g}: {bool(g)}') # True
print(f'bool of value PUSTA WARTOŚĆ: {bool(h)}') # False
print(f'bool of value SPACJA: {bool(i)}') # True



# OPERATORY IDETYCZNOŚCIOWE
# Określają, czy dwie zmienne przechowują ten sam obiekt. Mamy dwa operatory identycznościowe:
is
not is

x = "ala ma kota"
y = "ala nie ma kota"
if x is not y:
    print("Obiekty x i y to nie te same obiekty")
x = y
if x is y:
    print("Obiekty x i y to  te same obiekty")

# OPERATORY PRZYNALEŻNOŚCI
# Sprawdzają, czy dany element zawiera się w podzbiorze wartości danego obiektu. Mamy dwa takie operatory:
# in
# not in

x = "ala ma kota"
if "ma" in x:
    print("wyraz 'ma' występuje w ciągu'",x,"'")
y = [2, 3, 4, 100]
if 4 in y:
    print("Liczba 4 występuje w zbiorze",y)
else:
    print("Liczba 4 nie występuje w zbiorze",y)


# HIERARCHIA OPERATORÓW w Pythonie określa kolejność wykonywania poszczególne działania w wyrażeniu.
# Podobnie jak w matematyce, pewne operacje mają pierwszeństwo przed innymi. Jest to kluczowe dla uniknięcia błędów logicznych.
#
# 1. NAWIASY mają najwyższy priorytet.
# 2. OPERATORY ARYTMETYCZNE (w kolejności jak niżej):
#    – Potęgowanie
#    – Mnożenie, dzielenie, dzielenie całkowite, reszta z dzielenia
#    – Dodawanie i odejmowanie
# 3. OPERATORY PORÓWNANIA i PRZYNALEŻNOŚCI (w kolejności jak niżej):
#    – Porównania: ==, !=, >, <, >=, <=
#    – Przynależność i tożsamość: in, is
# 4. OPERATORY LOGICZNE (w kolejności jak niżej):
#    – not
#    – and
#    – or
# Ważne zasady:
# – Łączność lewostronna: Gdy operatory mają ten sam priorytet (np. mnożenie i dzielenie), działania są wykonywane po kolei od lewej do prawej strony wyrażenia.
# – Czytelność: Nawet jeśli znasz hierarchię, stosowanie nawiasów jest dobrą praktyką, ponieważ czyni kod bardziej czytelnym dla innych programistów.
