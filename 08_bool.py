####### Typy logicznie i operatory logiczne
# Typ danych BOOL (służący do reprezentowania wartości logicznych) przyjmuje jedną z dwóch wartości: True albo False
# True: reprezentuje logiczną PRAWDĘ
# False: reprezentuje logiczny FAŁSZ
# Wartości True i False muszą być zapisane zaczynając się od wielkiej litery

data_true = True
data_false = False

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



####### Operatory logiczne

# and (i): Zwraca True tylko wtedy, gdy oba warunki są prawdziwe.
# Aby wejść na koncert, musisz mieć ukończone 18 lat i mieć ważny bilet.
# Jeśli zabraknie choć jednej z tych rzeczy, to otrzymamy False.
print(f'Prawda i Prawda to: {True and True}') # True
print(f'Prawda i Fałsz to: {True and False}') # False
print(f'Fałsz i Fałsz to: {False and False}') # False
print()

# or (lub): Zwraca True, gdy przynajmniej jeden z warunków jest prawdziwy
# Możesz wejść do budynku, jeśli masz klucz lub jeśli ktoś Cię wpuści.
print(f'Prawda lub Prawda to: {True or True}') # True
print(f'Prawda lub Fałsz to: {True or False}') # True
print(f'Fałsz lub Fałsz to: {False or False}') # False
print()

# not (nie): Zaprzeczenie – zmienia True na False i odwrotnie
# Działa jak przełącznik światła.
print(f'Nie Prawda to: {not True}') # False
print(f'Nie Fałsz to: {not False}') # True
print()

print(f'Nie Prawda lub Fałsz to: {not True or False}') # False lub False = False
print(f'Nie Prawda lub Fałsz to: {not True or not False}') # False lub True = True
print(f'Nie (Prawda lub Fałsz) to: {not (True or False)}') # nie (True lub False) = False
print()



###### KONWERSJA na bool

print(bool(123)) # True
print(bool(-1)) # True
print(bool('abcd')) # True
print(bool(' '))  # True
print(bool('')) # False
print(bool(0)) # False
print(bool(0.0)) # False
print(bool(.0)) # False – 0.0 możemy też zapisać jako .0
