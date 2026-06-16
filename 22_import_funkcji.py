####### IMPORT FUNKCJI
#
# Przygotowana wcześniej FUNKCJA "get_random_numbers" znajduje się w katalogu "utils"
# Mogę ją zaimportować za kilka sposobów:

# 1. NAJLEPSZA PRAKTYKA to zaimportowanie FUNKCJI (get_random_numbers) z danego MODUŁU (utils.random_numbers).
# Używamy, kiedy potrzebujemy tylko jednej FUNKCJI.
# Gdzie "utils" to katalog na dysku, w którym znajduje się MODUŁ.

from utils.random_numbers import get_random_numbers # To jest nasz własny MODUŁ

zmienna = get_random_numbers(1,20,5)
print(zmienna)
print(len(zmienna))

# inny przykład

from utils.geom import circle_area, calculate_euclidean_distance

area = circle_area(5)
print(area)


# 2. Import pojedynczej funkcji (zAliasować).
# Używamy wtedy, kiedy z danej biblioteki chcemy używać więcej niż jednej funkcji.

import utils.random_numbers as my_package

zmienna = my_package.get_random_numbers(1,20,5)
print(zmienna)
print(len(zmienna))


# 3. Wczytywanie wszystkich funkcji. Ten sposób jest złą praktyką. Nie robimy tak.

from utils.random_numbers  import *

zmienna = get_random_numbers(1,20,5)
print(zmienna)
print(len(zmienna))



### MODUŁ "math" zawierający różne funkcjonalności matematyczne.
#

import math

print(math.sqrt(4)) # Pierwiastek
print(math.pi) # Liczba pi
print(math.e) # Liczba Eulera

p1 = (1, 2)
p2 = (4, 6)
euclidean_distance = math.dist(p1, p2)
print(euclidean_distance) # Dystans Euklidesowy – odległość między dwoma punktami / długość odcinka w układzie współrzędnych.
# Import FUNKCJI z MODUŁY math

my_dist = calculate_euclidean_distance(p1, p2)
print(my_dist) # MODUŁ zaimportowany w wierszu 18
# Import FUNKCJI z MODUŁU znajdującego się w "geom".


### MODUŁ "datetime" do pracy z czasem – pobieranie elementów z DATY
#
# https://docs.python.org/3/library/datetime.html?utm_source=chatgpt.com#strftime-and-strptime-format-codes

from datetime import datetime, date

teraz = datetime.now()
print(teraz) # Wyświetli datę i dokłądną godzinę: 2026-06-16 17:38:05.465284
print(f'Godzina: {teraz.hour} / Minuta: {teraz.minute} / Sekunda: {teraz.second}') # Godzina: 17 / Minuta: 45 / Sekunda: 21

dzisiaj = date.today()
print(dzisiaj) # Wyświetli datę: 2026-06-16
print(type(dzisiaj)) # <class 'datetime.date'>
print(date.today().year) # Wyświetli: 2026
print(f'Rok: {dzisiaj.year} / Miesiąc: {dzisiaj.month} / Dzień: {dzisiaj.day}') # Rok: 2026 / Miesiąc: 6 / Dzień: 16


### Formatowanie DATY na własny użytek

date_string = dzisiaj.strftime('%d.%m.%Y') # Wyświetli: 16.06.2026. Formatuje i ZAMIENIA na STRING.
# Gdzie: d – dzień, m – miesiąc, Y – rok.
print(date_string)
print(type(date_string)) # <class 'str'>


# Zamiana TEKSTU na STRING

text = '09-06-2026'
to_datetime = datetime.strptime(text, '%d-%m-%Y')
print(to_datetime) # Wyświetli: 2026-06-16 00:00:00
print(type(to_datetime)) # Wyświetli: <class 'datetime.datetime'>


# Operacje arytmetyczne na czasie

from datetime import timedelta

print(dzisiaj + timedelta(days=1)) # Wyświetli: 2026-06-17 – jutrzejszy dzień
