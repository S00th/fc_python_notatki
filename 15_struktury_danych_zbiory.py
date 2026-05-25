####### STRUKTURY DANYCH – ZBIORY {sets}

# – Zbiory {set}: Przechowują NIEUPORZĄDKOWANE kolekcje UNIKALNYCH ELEMENTÓW (DUPLIKATY, czyli dwie zmienne o takiej samej wartości są automatycznie usuwane).
#   MOŻEMY MODYFIKOWAĆ zawartość LISTY – możemy dodawać, zmieniać lub usuwać ELEMENTY.
#   MAGĄ zawierać różne TYPY DANYCH, np. lista = {12, True, 'Andrzej', 55.5}
#   Mogą zawierać duplikaty wartości, ale każdy duplikat traktuje jak jedną WARTOŚĆ.
#   NIE są strukturami INDEKSOWALNYMI. Nie jesteśmy w stanie określić, który element jest pierwszy, drugi itd. (worek z prezentami św. Mikołaja)
#   ZAPIS w nawiasach klamrowych {} lub set().
#   Są przydatne, kiedy nie interesuje nas liczba powtarzających się elementów, a jedynie unikalne wartości.
#   Przeszukiwanie po ZBIORACH jest szybszą operacją niż przeszukiwanie np. listy.


### TWORZENIE zbiorów

set_1 = {12, True, 'Andrzej', 55.5}
set_2 = set((12, True, 'Andrzej', 55.5))


### ODCZYTYWANIE zbiorów

print(set_1) # Wyświetl zawartość zbioru. UWAGA! Za każdym razem ELEMENTY zbioru zostaną wyświetlone w innej kolejności.
print(type(set_1)) # Sprawdź TYP DANYCH elementu -> <class 'set'>
print('Andrzej' in set_1) # Wyświetl czy dany element znajduje się w zbiorze.
for element in set_1: # Wyświetl zawartość zbioru. ZBIÓR jest obiektem iterowalnym, więc możemy na nim korzystać z pętli "for">
    print(element)    # Operacja ta będzie szybsza na ZBIORACH niż na LISTACH.


### Funkcja .add() – DODAWANIE elementu do zbioru.

set_1.add('Aga') # Dodaj element do zbioru.
print(set_1)
# UWAGA! Metoda .append() lub .insert() nie działa na ZBIORACH – działa tylko na LISTACH.


### Funkcja .remove() – USUWANIE elementu do zbioru.
set_1.remove('Aga') # Dodaj element do zbioru (za każdym razem wyświetli elementy w innej kolejności).
print(set_1)
# UWAGA! Metoda del nie działa na ZBIORACH – działa tylko na LISTACH.


### ZMIANA wartości na ELEMENCIE z listy na inną.

random_list[-1] = 'Ewa'
print(random_list)
