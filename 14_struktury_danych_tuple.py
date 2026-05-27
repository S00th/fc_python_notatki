####### STRUKTURY DANYCH – KROTKI (tuple)

# – Krotki (tuple): Przechowują UPORZĄDKOWANE kolekcje ELEMENTÓW (WARTOŚCI).
#   NIE MOŻEMY modyfikować zawartości krotki – nie możemy dodawać, modyfikować, ani usuwać ELEMENTÓW.
#   ZAWARTOŚĆ krotki JEST NIEZMIENNA (stała) od momentu utworzenia. Raz zadeklarowana krotka musi być taka sama przez cały czas trwania programu.
#   MAGĄ zawierać różne TYPY DANYCH, np. krotka = (12, True, 'Andrzej', 55.5)
#   Są strukturami INDEKSOWALNYMI.
#   Są strukturami ITEROWALNYMI.
#   ZAPIS – w nawiasach okrągłych () lub bez nawiasów (ale NIE ZAPISUJEMY ich w taki) lub tuple().
#   Są przydatne np. w formularzach, w których wymagamy wybrania jednej z sugestii (np. płeć: M / K)
#   tam, gdzie chcemy ZABLOKOWAĆ użytkownikowi możliwość DODANIA KOLEJNYCH OPCJI.



### TWORZENIE tupli

tuple_1 = (12, True, 'Andrzej', 55.5) # Jasne deklarowanie jest bardzo ważne
tuple_2 = 12, True, 'Andrzej', 55,5 # Taki zapis to też KROTKA, ale może być problematyczne, kiedy pomylimy KROPKĘ z PRZECINKIEM
liczba = 55,5 # W tym momencie mamy TUPLE, zamiast FLOATa.
tuple_3 = tuple((12, True, 'Andrzej', 55.5))


### ODCZYTYWANIE z tupli

print(type(tuple_1)) # Sprawdź TYP DANYCH elementu -> <class 'tuple'>
print(tuple_1) # Wyświetl zawartości tuple
print(tuple_1[0]) # Wyświetl konkretnego ELEMENTU
print(tuple_1.index('Andrzej')) # Pokaż INDEX konkretnego ELEMENTU
print(tuple_1[0:3]) # Wyświetl ZAKRES ELEMENTÓW
# print(uczestnicy[7]) # Jeżeli wskażemy element spoza krotki, wyświetli się BŁĄD

for element in krotka_1: # Wyświetl zawartość tupli. TUPLA jest obiektem iterowalnym, więc możemy na nim korzystać z pętli "for"
    print(element)



####### Czy tupla może myć KLUCZEM w SŁOWNIKU?

list = ['Adam', 15, 15.5, True]
tuple = ('Adam', 15, 15.5, True)
set = {'Adam', 15, 15.5, True}
dict = {'name': 'Ewa', 'age': 20 }

print(list)
print(type(list))
print()

print(tuple)
print(type(tuple))
print()

print(set)
print(type(set))
print()

print(dict)
print(type(dict))
print()

dict2 = {('Adam', 15, 15.5, True): 'Ewa', 'age': 20 }
print(dict2)
print(type(dict2))
