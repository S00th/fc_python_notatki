####### STRUKTURY DANYCH
#
# STRUKTURY DANYCH to specjalne SPOSOBY ORGANIZOWANIA, PRZECHOWYWANIA i ZARZĄDZANIA INFORMACJAMI w programie,
# które pozwalają, na ich wydajne wykorzystywanie i przetwarzanie.
# Wszystkie struktury danych są ELEMENTAMI iterowalnymi, więc będziemy mogli na ich podstawie korzystać z pętli "for".
# W liście mogą się znaleźć różne typy danych, np. uczestnicy = [12, True, 'Andrzej', 55.5].
# W trakcie działania programu możemy DODAĆ do listy nowe elementy.
# Zrozumienie ich działania jest niezbędne, aby przejść od prostego pisania składni do prawdziwego rozwiązywania problemów programistycznych.
#
# Podstawowe struktury wbudowane:
#
# – Listy [list]: to kontener przechowujący WIELE WARTOŚCI/ELEMENTÓW? (nawet różnych typów), w którym kolejność ma znaczenie.
#   W nawiasach kwadratowych []
#   Wartości są uporządkowane i MOŻNA ZMIENIĆ ich zawartość. LISTA jest przechowywana jako jedna wartość, która może być przypisana do zmiennej.
#
# – Krotki (tuple): Podobne do list, ale ICH ZAWARTOŚĆ JEST NIEZMIENNA (stała) po utworzeniu.
#   Nie można modyfikować, dodawać, ani usuwać elementów wewnątrz krotki. Krotka musi być taka sama podczas trwania całego programu.
#   W nawiasach () lub bez nawiasów (tak nie robimy). Mogą zawierać RÓŻNE wartości. Elementy krotki SĄ indeksowalne. Są iterowalne.
#   Są przydatne, kiedy mamy formularz do lekarza (płeć: M / K) i wymagamy wybrania jednej z sugestii – blokujemy dodanie kolejnych opcji.
#
# – Zbiory {set}: Przechowują UNIKALNE WARTOŚCI (możemy mieć duplikaty wartości, ale każdy duplikat traktuje jak jeden), co jest przydatne np. przy eliminowaniu duplikatów.
#   W nawiasach klamrowych {} lub set(). Mogą zawierać RÓŻNE wartości. Elementy zbioru NIE SĄ indexowalne.
#   MOŻNA modyfikować, dodawać i usuwać elementów wewnątrz zbioru.
#   Są przydatne, dla sklepów działające metodą dropów z eventami (kubki są unikalne, każdy inny). Przeszukiwanie po ZBIORACH jest szybszą operacją (niż np. listy).
#

Wszystkie 3 wczesniej przechowuja WARTOŚCI

# – Słowniki {dict}: Przechowują DANE W PARACH KLUCZ-WARTOŚĆ. Klucz określa, czym jest dany element w słowniku.
#   Pozwalają na bardzo szybkie odnajdywanie informacji na podstawie unikalnego klucza. Coś w rodzaju pęku kluczy.
#   W nawiasach klamrowych {'imie': "Michał", "wiek": 12}. Elementy krotki SĄ indeksowalne – w nawiasie kwadratowym wpisujemy KLUCZ (tu wyświetli błąd) lub metodą słownik.get() ta metoda jest bezpieczniejsza.
#   MOŻNA modyfikować, dodawać i usuwać elementy wewnątrz słownika (pamiętamy o unikalności wartości). Są iterowalne, ale w specyficzny sposób.
#   Nie wysztsko moze być kluczem wewnatrz słownika
!!! CO MOZE BYC / nie moze być KLUCZEM WEWNATRZ SŁOWNIKA? Pytanie na rozmowie kwalifikacyhnej?
str jest hashowalny

####### LISTY
#
# Listy definiujemy tak samo, jak zmienne, ale zbiór zmiennych dodajemy w NAWIASACH KWADRATOWYCH.
# LISTA jest obiektem iterowalnym.

uczestnicy = ['Marian', 'Jadwiga', 'Mariola', 'Andrzej', 'Richard']
# Z punktu widzenia komputera, różnica między tym, co wyżej, a tym, co niżej jest ogromna.
# Komputer wie, że zmienne wyżej są ze sobą połączone.
uczestnik_1 = 'Marian'
uczestnik_2 = 'Jadwiga'
uczestnik_3 = 'Mariola'
uczestnik_4 = 'Andrzej'
uczestnik_5 = 'Richard'

# Lista może być pusta.
lista_ocen = []
print(lista_ocen)

# lista_ocen_2 = list() # To nie po Pythonowemu.


### ODCZYTYWANIE z listy

# Aby sprawdzić TYP DANYCH elementu:
print(type(uczestnicy))


# Struktury danych, które bedą strukturami indeksowalnymi bedą się indeksować od zera.
# Każde element wewnątrz listy ma swój unikany indeks.

# Aby dostać się do konkretnego ELEMENTU z listy:
print(uczestnicy[0]) # Jeżeli wskażemy element spoza listy, wyświetli się BŁĄD.
# print(uczestnicy[7]) # Jeżeli wskażemy element spoza listy, wyświetli się BŁĄD.

# Aby dowiedzieć się, jaki INDEX ma konkretny ELEMENTU z listy:
print(uczestnicy.index('Andrzej'))

# Aby wyświetlić ZAKRES ELEMENTÓW z listy:
print(uczestnicy[0:3])




#### LISTA jest obiektem iterowalnym, więc możemy na jej podstawie korzystać z pętli "for".

for uczestnik in uczestnicy:
    print(uczestnik)



### Funkcja .append() – DODAWANIE element do listy na końcu listy.

random_list = [12, True, 'Andrzej', 55.5]

random_list.append('Aga') # Dodaj element na końcu listy.
print(random_list)



### Funkcja .insert() – DODAWANIE element do listy na końcu listy jako konkretny index.

random_list.insert(1, 'Aga') # Dodaj element jako konkretny index.
print(random_list)



### ZMIANA wartości na ELEMENCIE z listy na inną.

random_list[-1] = 'Ewa'
print(random_list)




### Funkcja .remove() – USUWANIE elementu z listy.

random_list.remove('Ewa')
print(random_list)
# lub
del random_list[0] # działa tylko na listach
print(random_list)



####### TUPLE
#

####### SŁOWNIKI
#


####### ZBIORY
#


#######
