####### STRUKTURY DANYCH – ZBIORY {sets}

# – Zbiory {set}: Przechowują NIEUPORZĄDKOWANE kolekcje UNIKALNYCH ELEMENTÓW (DUPLIKATY, czyli dwie zmienne o takiej samej wartości są automatycznie poomijane).
#   MOŻEMY usuwać i dodawać ELEMENTY ZBIORÓW, ale nie możemy ich modyfikować.
#   MAGĄ zawierać różne TYPY DANYCH, np. lista = {12, True, 'Andrzej', 55.5}
#   Mogą zawierać duplikaty wartości, ale każdy duplikat traktuje jak jedną WARTOŚĆ.
#   NIE są strukturami INDEKSOWALNYMI. Nie jesteśmy w stanie określić, który element jest pierwszy, drugi itd. (worek z prezentami św. Mikołaja)
#   ELEMENTY zbioru za każdym razem wyświetlą się w innej kolejności.
#   ZAPIS w nawiasach klamrowych {} lub set().
#   Są przydatne, kiedy nie interesuje nas liczba powtarzających się elementów, a jedynie unikalne wartości.
#   Przeszukiwanie po ZBIORACH jest szybszą operacją niż przeszukiwanie np. listy.


### TWORZENIE zbiorów

set_1 = {12, True, 'Andrzej', 55.5}
set_2 = set((12, True, 'Andrzej', 55.5))
set_3 = {12, False, 'Ewa', 55.5, 1000}

### ODCZYTYWANIE zbiorów

print(set_1) # Wyświetl zawartość zbioru. UWAGA! Za każdym razem ELEMENTY zbioru zostaną wyświetlone w innej kolejności.
print(type(set_1)) # Sprawdź TYP DANYCH elementu -> <class 'set'>
print('Andrzej' in set_1) # Wyświetl czy dany element znajduje się w zbiorze.
for element in set_1: # Wyświetl zawartość zbioru. ZBIÓR jest obiektem iterowalnym, więc możemy na nim korzystać z pętli "for">
    print(element)    # Operacja ta będzie szybsza na ZBIORACH niż na LISTACH.



### DODAWANIE elementu do zbioru – Funkcja .add()

set_1.add('Aga') # Dodaj element do zbioru.
print(set_1)
# UWAGA! Metoda .append() lub .insert() nie działa na ZBIORACH – działa tylko na LISTACH.


### USUWANIE elementu do zbioru – Funkcja .remove()

set_1.remove('Aga') # Dodaj element do zbioru (za każdym razem wyświetli elementy w innej kolejności).
print(set_1)
# UWAGA! Metoda del nie działa na ZBIORACH – działa tylko na LISTACH.


### ODEJMOWANIE jednego ZBIORU od drugiego
print(set_1 - set_3)


### Pobieranie CZĘŚCI WSPÓLNEJ kilku ZBIORÓW (elementów, które ŁĄCZĄ oba zbiory)
print(set_1 & set_3)


### Pobieranie CZĘŚCI ROZŁĄCZNEJ kilku ZBIORÓW (elementów, które NIE ŁĄCZĄ zbiorach)
print(set_2 ^ set_3)
