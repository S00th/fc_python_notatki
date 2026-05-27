####### STRUKTURY DANYCH i LISTY
#
# STRUKTURY DANYCH to "kontenery" / specjalne SPOSOBY ORGANIZOWANIA, PRZECHOWYWANIA i ZARZĄDZANIA INFORMACJAMI w programie,
# które pozwalają, na ich wydajne wykorzystywanie i przetwarzanie.
# Podstawowe struktury danych w Pythonie to LISTY, KROTKI, ZBIORY oraz SŁOWNIKI. Każda z nich ma odmienną budowę i inne zastosowania.
# Wszystkie struktury danych są ELEMENTAMI iterowalnymi, więc będziemy mogli na ich podstawie korzystać z pętli "for".
# Zrozumienie działania struktur danych jest NIEZBĘDNE, aby przejść od prostego pisania składni do prawdziwego rozwiązywania problemów programistycznych.
# Struktury danych możemy dzielić na STRUKTURY PROSTE i STRUKTURY ZŁOŻONE, ale też na ZMIENIALNE i NIEZMIENIALNE (HASHOWALNOŚĆ).

# ELEMENTY to pojedynczy obiekt (np. liczba, tekst) znajdujący się wewnątrz kontenera danych.
# O ELEMETACH mówimy, gdy wrzucamy rzeczy do "worka" (zbioru) lub ustawiamy je w "kolejce" (liście).
# O WARTOŚCIACH mówimy najczęściej wtedy, gdy dane są przypisane do konkretnych etykiet (kluczy w słowniku) lub nazw zmiennych.

# Podstawowe struktury wbudowane (struktury PŁASKIE – zawierające TYPY proste):

# – Listy [list]: Przechowują UPORZĄDKOWANE kolekcje ELEMENTÓW (WARTOŚCI).
#   MOŻEMY MODYFIKOWAĆ zawartość LISTY – możemy dodawać, zmieniać lub usuwać ELEMENTY.
#   MAGĄ zawierać różne TYPY DANYCH, np. lista = [12, True, 'Andrzej', 55.5]
#   Są strukturami INDEKSOWALNYMI. Każde kolejny element ma swoje unikalne miejsce.
#   Są strukturami ITEROWALNTMI.
#   LISTA jest przechowywana jako jedna wartość, która może być przypisana do ZMIENNEJ.
#   ZAPIS – w nawiasach kwadratowych []

# – Krotki (tuple): Przechowują UPORZĄDKOWANE kolekcje ELEMENTÓW (WARTOŚCI).
#   NIE MOŻEMY modyfikować zawartości krotki – nie możemy dodawać, modyfikować, ani usuwać ELEMENTÓW.
#   ZAWARTOŚĆ krotki JEST NIEZMIENNA (stała) od momentu utworzenia. Raz zadeklarowana krotka musi być taka sama przez cały czas trwania programu.
#   MAGĄ zawierać różne TYPY DANYCH, np. krotka = (12, True, 'Andrzej', 55.5)
#   Są strukturami INDEKSOWALNYMI.
#   Są strukturami ITEROWALNYMI.
#   ZAPIS – w nawiasach okrągłych () lub bez nawiasów (ale NIE ZAPISUJEMY ich w taki) lub tuple().
#   Są przydatne np. w formularzach, w których wymagamy wybrania jednej z sugestii (np. płeć: M / K)
#   tam, gdzie chcemy ZABLOKOWAĆ użytkownikowi możliwość DODANIA KOLEJNYCH OPCJI.

#   Różnica między LISTĄ i KROTKĄ modyfikacji wartości znajdujących się w tych zbiorach danych (LISTĘ można modyfikować, a TUPLI nie).

# – Zbiory {set}: Przechowują NIEUPORZĄDKOWANE kolekcje UNIKALNYCH ELEMENTÓW (DUPLIKATY, czyli dwie zmienne o takiej samej wartości są automatycznie usuwane).
#   MOŻEMY MODYFIKOWAĆ zawartość LISTY – możemy dodawać, zmieniać lub usuwać ELEMENTY.
#   MAGĄ zawierać różne TYPY DANYCH, np. lista = {12, True, 'Andrzej', 55.5}
#   Mogą zawierać duplikaty wartości, ale każdy duplikat traktuje jak jedną WARTOŚĆ.
#   NIE są strukturami INDEKSOWALNYMI. Nie jesteśmy w stanie określić, który element jest pierwszy, drugi itd. (worek z prezentami św. Mikołaja)
#   ZAPIS w nawiasach klamrowych {} lub set().
#   Są przydatne, kiedy nie interesuje nas liczba powtarzających się elementów, a jedynie unikalne wartości.
#   Przeszukiwanie po ZBIORACH jest szybszą operacją niż przeszukiwanie np. listy.

#   LISTY, TUPLE i ZBIORY są zbiorami danych, w których znajdują się tylko i wyłącznie ELEMENTY.
#   LISTY i TUPLE są indeksowane, a ZBIORY nie.

# – Słowniki {dict}: Przechowują UPORZĄDKOWANE kolekcje w PARACH KLUCZ-WARTOŚĆ. KLUCZ określa, czym jest dany ELEMENT w słowniku.
#   MOŻEMY MODYFIKOWAĆ zawartość LISTY – możemy dodawać, zmieniać lub usuwać ELEMENTY (pamiętając o unikalności wartości).
#   Pozwalają na bardzo szybkie odnajdywanie informacji na podstawie unikalnego klucza. Są czymś w rodzaju pęku kluczy.
#   Są strukturami INDEKSOWALNEMI, ale w specyficzny sposób.
#   Są strukturami ITEROWALNEMI, ale w specyficzny sposób.
#   ZAPIS – w nawiasach klamrowych {}, w których znajdują się pary KLUCZ-WARTOŚĆ {'imie': "Michał", "wiek": 12}.
#   Wewnątrz słownika NIE WSZYSTKO MOŻE BYC KLUCZEM!!!

# Wewnątrz SŁOWNIKÓW nie wszystko może być KLUCZEM – możemy definiować jako KLUCZE, tylko niektóre obiekty.
# Klucze MUSZĄ być NIEZMIENNE (ang. IMMUTABLE) i HASZOWALNE, aby słownik mógł poprawnie i trwale obliczać ich skróty (HASZE).
# Różnica między niemutowalnością, a hashowalnością wynika z ich roli w zarządzaniu danymi:
# niemutowalność dotyczy tego, czy obiekt można zmienić,
# natomiast hashowalność określa, czy obiekt może być użyty jako unikalny identyfikator w strukturach takich jak słowniki.
#
# Np. STRING jest HASHOWALNY / NIEMUTOWALNY.
# Kluczami NIE MOGĄ być żadne obiekty MUTOWALNE (zmienne), takie jak:
# LISTY ['a', 'b']
# ZBIORY {1, 2, 3}
# SŁOWNIKI {'wiek': 30}
#
# Pytanie podczas rekrutacji: CO MOŻE BYĆ KLUCZEM WEWNĄTRZ SŁOWNIKA?


####### LISTY [12, True, 'Andrzej', 55.5]
# Listy definiujemy tak samo, jak ZMIENNE, ale LISTĘ (ZBIÓR zmiennych) dodajemy w NAWIASACH KWADRATOWYCH.
# LISTA jest obiektem iterowalnym.

list = ['Marian', 'Jadwiga', 'Mariola', 'Andrzej', 'Richard']
# Z punktu widzenia komputera, różnica między tym, co wyżej, a tym, co niżej jest ogromna.
# Komputer wie, że zmienne wyżej są ze sobą połączone.
uczestnik_1 = 'Marian'
uczestnik_2 = 'Jadwiga'
uczestnik_3 = 'Mariola'
uczestnik_4 = 'Andrzej'
uczestnik_5 = 'Richard'

### TWORZENIE listy.

list_1 = ['5', '4', '3', '2', '1']
list_2 = [] # Lista może być pusta.
list_3 = list() # Ten zapis jest nie po Pythonowemu.


### ODCZYTYWANIE z listy

print(type(list_1)) # Sprawdź TYP DANYCH elementu -> <class 'list'>
print(list_1[0]) # Wyświetl konkretnego ELEMENTU
print(list_1.index('Andrzej')) # Pokaż INDEX konkretnego ELEMENTU
print(list_1[0:3]) # Wyświetl ZAKRES ELEMENTÓW
# print(list[7]) # Jeżeli wskażemy element spoza krotki, wyświetli się BŁĄD


#### LISTA jest obiektem iterowalnym, więc możemy na jej podstawie korzystać z pętli "for".

for uczestnik in uczestnicy:
    print(uczestnik)


### Funkcja .append() – DODAWANIE elementu do listy NA KOŃCU listy.

random_list = [12, True, 'Andrzej', 55.5]

random_list.append('Aga') # Dodaj element na końcu listy.
print(random_list)


### Funkcja .insert() – DODAWANIE elementu do listy JAKO KONKRETNY INDEX.

random_list.insert(1, 'Aga') # Dodaj element jako konkretny index (najpierw podajemy INDEX, a później ELEMENT).
print(random_list)


### ZMIANA wartości na ELEMENCIE z listy na inną.

random_list[-1] = 'Ewa'
print(random_list)


### Funkcja .remove() – USUWANIE elementu z listy.

random_list.remove('Ewa') # Używaj tej metody
print(random_list)
# lub
del random_list[0] # Metoda del działa tylko na LISTACH
print(random_list)



###### HASHOWALNOŚĆ danych.
# Struktury danych możemy dzielić na STRUKTURY PROSTE i STRUKTURY ZŁOŻONE, ale też na ZMIENIALNE i NIEZMIENIALNE.

name = 'Michał'
print(id(name)) # Wyświetli np. 1992162399840

name = 'Andrzej'
print(id(name)) # Wyświetli np. 1992162889856

# Wyświetlone zostały inna wartość, co oznacza, że gdy wyświetlimy wartość zmiennej,
# to tak na prawe nie zmieniamy jej wartości, a USUWAMY starą zmienną i TWORZYMY nową.
# Dzieje się tak też w przypadku INTEGERów.

lista = ['Adam', 'Michał']
print(id(lista))

lista[0] = 'Ewa'
print(id(lista))

# Natomiast, kiedy zmieniamy element w LISTACH, to będziemy modyfikować element – mówimy, że listy są MUTOWALNE.
# Oznacza to, że możesz swobodnie zmieniać, dodawać lub usuwać ich elementy bez konieczności tworzenia nowego obiektu i w tym samym miejscu w pamięci.

# Wewnątrz SŁOWNIKÓW nie wszystko może być KLUCZEM – możemy definiować jako KLUCZE, tylko niektóre obiekty.
# Klucze MUSZĄ być niezmienne (ang. immutable) i HASZOWALNE, aby słownik mógł poprawnie i trwale obliczać ich skróty (HASZE).
# Np. STRING jets HASHOWALNY / NIEMUTOWALNY.
# Kluczami NIE MOGĄ być żadne obiekty MUTOWALNE (zmienne), takie jak:
# LISTY ['a', 'b']
# ZBIORY {1, 2, 3}
# SŁOWNIKI {'wiek': 30}
#
# Pytanie podczas rekrutacji: Co może myć kluczem wewnątrz SŁOWNIKA?
