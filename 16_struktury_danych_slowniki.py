####### STRUKTURY DANYCH – SŁOWNIKI {dict}

# – Słowniki {dict}: Przechowują UPORZĄDKOWANE kolekcje w PARACH KLUCZ-WARTOŚĆ. KLUCZ określa, czym jest dany ELEMENT w słowniku.
#   MOŻEMY MODYFIKOWAĆ zawartość LISTY – możemy dodawać, zmieniać lub usuwać ELEMENTY (pamiętając o unikalności wartości).
#   Pozwalają na bardzo szybkie odnajdywanie informacji na podstawie unikalnego klucza. Są czymś w rodzaju pęku kluczy.
#   Są strukturami INDEKSOWALNEMI, ale w specyficzny sposób.
#   Są strukturami ITEROWALNEMI, ale w specyficzny sposób.
#   ZAPIS – w nawiasach klamrowych {}, w których znajdują się pary KLUCZ-WARTOŚĆ {'imie': "Michał", "wiek": 12}.
#   Wewnątrz słownika NIE WSZYSTKO MOŻE BYC KLUCZEM!!!

# Wewnątrz SŁOWNIKÓW nie wszystko może być KLUCZEM – możemy definiować jako KLUCZE, tylko niektóre obiekty.
# Klucze MUSZĄ być niezmienne (ang. immutable) i HASZOWALNE, aby słownik mógł poprawnie i trwale obliczać ich skróty (HASZE).
# Np. STRING jest HASHOWALNY / NIEMUTOWALNY.
# Kluczami NIE MOGĄ być żadne obiekty MUTOWALNE (zmienne), takie jak:
# LISTY ['a', 'b']
# ZBIORY {1, 2, 3}
# SŁOWNIKI {'wiek': 30}
#
# Pytanie podczas rekrutacji: CO MOŻE BYĆ KLUCZEM WEWNĄTRZ SŁOWNIKA?





### TWORZENIE słowników

dict = {'name': 'Adam', 's_name': 'Kowalski', 'age': 12, 'class': '1e'}
# inny zapis
dict= {
    'name': 'Adam',
    's_name': 'Kowalski',
    'age': 12,
    'class': '1e'
}


### ODCZYTYWANIE ze słownika

print(type(dict)) # Sprawdź TYP DANYCH elementu -> <class 'list'>
print(dict) # Wyświetl zawartość słownika.
print(dict.keys()) # Wyświetl klucze.
print(dict.values()) # Wyświetl wartości
print(dict.items()) # Wyświetli się lista TUPLI: dict_items([('name', 'Adam'), ('s_name', 'Kowalski'), ('age', 12), ('class', '1e')])
print(dict.get('name')) # Wyświetl konkretny ELEMENT słownika – BEZPIECZNIEJSZY SPOSÓB
# print(dict['name']) # Wyświetl konkretny ELEMENT słownika (nie używamy tego sposobu) -> print(dic['KLUCZ'])
# print(dic['rozmiar_buta']) # Jeżeli wskażesz element spoza słownika, wyświetli się BŁĄD


### DODAWANIE i EDYCJA elementu do słownika – NA KOŃCU słownika.

dict['waga'] = 55 # <nazwa słownika>['KLUCZ'] = WARTOŚĆ
# UWAGA! Dodawanie i edycja w słowniku jest operacją tożsamą.
# Zawsze, kiedy dodam KLUCZ, który już znajduje się w słowniku, zmodyfikujemy WARTOŚĆ przypisaną do KLUCZA.
# KLUCZE znajdujące się wewnątrz struktury słownika muszą być kluczami UNIKALNYMI (nie może być 2 kluczy do tej samej sali).

#dict[[1, 2, 3]] = oceny <- Nie jesteśmy w stanie dodać LISTY jako KLUCZA w SŁOWNIKU, ponieważ LISTA jest NIEHASHOWALNA.
#dict[{1, 2, 3}] = oceny <- Nie jesteśmy w stanie dodać ZBIORU jako KLUCZA w SŁOWNIKU, ponieważ ZBIÓR jest NIEHASHOWALY.
#dict['oceny] = [1, 2, 3] <- To jesteśmy w stanie zrobić – LISTA może być WARTOŚCIĄ w SŁOWNIKU.


### USUWANIE elementu ze słownika.

dict.pop('name')
# lub
del dict['name'] # Tem sposób też zadziała, ale raczej go nie używamy


#### ITERACJA słownika
# Słowniki są iterowalne, więc możemy na nich korzystać z pętli "for".

for uczestnik in dict.keys(): # Zmienną w pętli for możemy nazwać w dowolny sposób, ale róbmy to w sposób jasny.
    print(uczestnik) # ITERACJA wyłącznie po KLUCZACH naszego SŁOWNIKA – tu robi to świadomie.

for value in dict.values(): # ITERACJA wyłącznie po WARTOŚCIACH naszego SŁOWNIKA.
    print(value)

for key, value in dict.items(): # ITERACJA po ITEMSach (czyli po KLUCZACH i WARTOŚCIACH) naszego SŁOWNIKA.
    print(f' Klucz: {key} + wartość: {value}')



####### ĆWICZENIE – Iteracja przez SŁOWNIK

slownik = {1: 'Asia', 2: 'Basia', 3: 'Marta', 4: 'Danusia'}

for val in slownik.values(): # Iteracja przez WARTOŚCI słownika
    print(val)

for key in slownik.keys(): # Iteracja przez KLUCZE słownika
    print(key)

for item in slownik.items(): # Iteracja przez KLUCZE i WARTOŚCI słownika
    print(item) # wyświetli WARTOŚĆ słownika zamienioną na TUPLE (zbiory złożone) składających się z par KLUCZ i WARTOŚĆ

for item in slownik.items(): # Iteracja przez KLUCZE i WARTOŚCI słownika
    print(item[0], item[1]) # Wyświetli osobno jako INTERGER i TEKST
    slownik[item[0]] = 'WIKTOR'


for key, val in slownik.items(): # Iteracja przez KLUCZE i WARTOŚCI słownika
    print(f'KEY: {key} VA: {val}')


####### ĆWICZENIE – Zamień miejscami klucze i wartości

dict = {'IMIE': 'Adam', 'NAZWISKO': 'Kowalski', 'WIEK': 12, 'KLASA': '1e'}

new_dict = {}
for item in dict.items():  # Iteracja przez KLUCZE i WARTOŚCI słownika
    print(item[0], item[1])  # Wyświetli osobno jako INTERGER i TEKST
    new_dict[item[1]] = item[2]

print(dict)
print(new_dict)



####### ĆWICZENIE – Jak miał na imię elf z LotR?

# hero = {'Czarodziej': 'Gandalf', 'Elf': 'Legolas', 'Krasnolud': 'Gimli'}
#
# question = input('Jaka jest stolica Polski? ')
# if hero['Polska'] == question:
#     print('Brawo.')
# else:
#     print(f'Niestety nie jest to {question}. Chodziło o {hero['Czarodziej']}.')



### Przykład STRUKTURY ZŁOŻONEJ
# UWAGA! Jeśli chcielibyśmy stworzyć LISTĘ uczniów, będziemy musieli stworzyć strukturę złożoną – LISTĘ SŁOWNIKÓW.
#
# uczniowie = [
#     {
#         'imie': 'Anna',
#         'nazwisko': 'Nowak'
#     },
#     {
#         'imie': 'Ewa',
#          'nazwisko': 'Kowalska'
#     }
# ]