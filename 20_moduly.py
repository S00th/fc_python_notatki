####### MODUŁY
#
# Im bardziej skomplikowane będą nasze projekty, tym bardziej będziemy potrzebowali dodatkowych funkcjonalności.
# Oczywiście mamy funkcje BUDOWANE, dostępne w każdym module Pythona, których nie trzeba importować,
# ale nie zawsze tak będzie. Dlatego istnieje coś takiego jak BIBLIOTEKA STANDARDOWA – instaluje się wraz z Pythonem.
# BIBLIOTEKA STANDARDOWA to zestaw wbudowanych funkcjonalności, które trzeba ZAIMPORTOWAĆ, ale nie trzeba instalować.
# Biblioteko importujemy przy pomocy słowa kluczowego "import".
# Przykłady bibliotek: random, string, math, datetime.
#
# Dodatkowo mamy też: PAKIETY, BIBLIOTEKI i FRAMEWORKi.
# Są to funkcjonalności ogólnego użycia, które ktoś już napisane i trzeba je zainstalować i zaimportować.
# Przykłady bibliotek: pandas, django, fastapi, scikit-learn, flask.
# pypi.org – Publiczne repozytorium, z którego można pobierać pakiety (np. pandas). Można też publikować własne.
# Pakiet Wiktora (polymorvic): cvgeomkit 0.1.4 (2026.06) – zestaw funkcjonalności.
# Pakiet to kod Pythona, który ma zdefiniowane różne rzeczy.
# To, z jakich pakietów będziemy korzystać, będzie zdeterminowane specjalizacją/zadaniami, które będziemy wykonywać.
#
# MODUŁY WŁASNE to funkcjonalności zdefiniowane samemu, stworzone na potrzeby konkretnego projektu.
# Do zastosowania w obszarze, w którym jeszcze nikt nie napisał potrzebnych nam funkcjonalności.

# Przykłady FINKCJI z MODUŁY random
#
# import random
# random.randint(<arg1>, <arg2>):
# MODUŁ losuje jedną (pseudo)losową liczbę całkowitą podanego z zakresu (<początek_zakresu>, <koniec_zakresu>)

import random

num = random.randint(10, 40)
print(num)

# Ziarno losowe dla powtórzenia wyników losowania (powtórzenie wyniku losowania).
random.seed(123) # Jeśli nie zmienię wartości w nawiasie, to mam zagwarantowane, że wylosuje się zawsze to samo.
num2 = random.randint(10, 40)
print(num2)

names = ['Asia', 'Basia', 'Danusia']
random_name = random.choice(names) # Losuje element ze zbiory zmiennych
print(random_name)



### ZADANIE
#
# Napisz FUNKCJĘ, która zwróci listę unikanych liczb losowych z zadanego zakresu o zadanej długości elementów.
#
# ETAP 1

import random

lista = []
max_len = 10 # Chcę 10 liczb w liście
start_range = 1
end_range = 20
while len(lista) < max_len: # Sprawdza, czy w LISTA (jej zawartość) jest mniejsza niż 10 (przy 10 skończy się wykonywać)
    random_num = random.randint(start_range,end_range)
    if random_num not in lista: # Zanim dodamy liczbę do LISTY, sprawdzamy, czy liczba jest już na LIŚCIE.
        lista.append(random_num) # w przeciwnym wypadku nie jest potrzebne.
print(lista)
print(len(lista))

# ETAP 2 – Przygotowanie FUNKCJI

def get_random_numbers(start_range: int, end_range: int, out_len: int) -> list[int]:
    if out_len > (end_range - start_range) + 1: # Aby zapobiec sytuacji, w której ZAKRES +1 jest większy niż DŁUGOŚĆ
        raise ValueError(f'Out_len={out_len} is out of range')
    numbers_list = []
    while len(numbers_list) < out_len:
        num = random.randint(start_range, end_range)
        if num not in numbers_list:
            numbers_list.append(num)
    return numbers_list
zmienna = get_random_numbers(1,20,5)

print(zmienna)
print(len(zmienna))