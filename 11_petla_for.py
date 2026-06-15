####### PĘTLA "for" (pętla ITERACYJNA)
#
# PĘTLA "for" (pętla ITERACYJNA) wykonuje się SKOŃCZONA/OKREŚLONĄ ilość razy.
# Używana, gdy znamy LICZBĘ POWTÓRZEŃ danej OPERACJI lub gdy do czynienia z OGRANICZONYM ZBIOREM danych (LISTA lub SŁOWNIK).
# ZAKOŃCZY SIĘ w momencie, kiedy skończy się ZBIÓR DANYCH (kiedy zakończy się obiekt ITEROWALNY).
# Przykładem obiektu ITEROWALNEGO jest ZAKRES LICZB lub STRING (ponieważ słowo możemy PRZEITEROWAĆ).
# bool, int i float nie są obiektami ITEROWALNYMI.
# W programowaniu często stosuje się PĘTLĘ FOR w konstrukcji "for in range", która pozwala na precyzyjne określenie liczby powtórzeń.

# Uwaga: instrukcje CONTINUE i BREAK również działają w pętlach "for".
# W PĘTLI "for" również działa klauzula "else".

# WAŻNE!
# Podstawową różnicą ułatwiającą zapamiętanie obu konstrukcji jest to,
# że pętla "while" działa tak długo, jak spełniony jest określony WARUNEK,
# natomiast pętla "for" operuje na OBIEKCIE ITEROWALNYM.


# WAŻNE! Aby przerwać uruchomioną, niekończącą się pętle, wciskamy ctrl + c.


### SKŁADNIA
#
# for <tymczasowa_zmienna> in <obiekt_iterowalny>:>
    # kod wewnątrz pętli <blok kodu>

# for <- słowo kluczowe.
# <tymczasowa_zmienna> <- żyje tylko w momencie pętli "for".
# Podczas ITEROWANIA <obiekt_iterowalny>, to przy każdej kolejnej ITERACJI pętli <tymczasowa_zmienna> będzie przyjmowała wartość kolejnego elementu zbioru danych.
# in <- słowo kluczowe.
# <obiekt_iterowalny> <- zmienna STRING, ZAKRES LICZB lub STRUKTURA DANYCH.


for num in range(5): # range(5) zwraca nam wartości od 0 do 4, a num będzie przechowywał te wartości po kolei.
    print(num) # Program przeszedł przez wszystkie wartości i je wyświetlił.

# Kiedy chce wyświetlić jakiś komunikat konkretną ilość razy
for _ in range(5):
    print('Cześć. ')



### ITERACJA przez listę
#
names = ['Asia', 'Dasia', 'Danusia']

for name in names: # Pętla: sięga do listy, wyciąga pierwszy obiekt, drukuje go i wraca do listy. Robi tak az, skończą się obiekty w liście i wychodzi.
    print(name)



### ĆWICZENIE, dodaj 10 do każdej liczby w liście
#
numbers = [1, 2, 3]

for number in numbers:
    plus_10 = number+10
    print(plus_10)



#### ĆWICZENIE – Oblicz sumę liczb
#
# Oblicz sumę INTEGERÓW przy pomocy pętli "for".

numbers = [1, 2, 3]

sum = 0 # Początkowa suma wynosi zero
for number in numbers:
    sum += number # Dodawana jest pierwsza WARTOŚĆ z listy do SUMY, a następnie druga wartość, trzecia wartość i następuje wyjście z pętli.
    print(sum)



### ĆWICZENIE – Przez jakie liczby jest podzielna podana liczba?

nasza_liczba = int(input('Podaj swoją liczbę: '))

for liczba in range(1, nasza_liczba):
    if nasza_liczba % liczba == 0:
        print(f'{nasza_liczba} jest podzielna przez {liczba}]')
    # if nasza_liczba % 3 == 0:
    #     print('Liczba jest podzielna przez 3')

# renge() <- ITERATOR, a nie funkcja, ale chwilowo traktujemy go jak funkcję ;)
# w nawiasie podajemy: range(<zakres_początkowy>, <zakres końcowy>)



# ĆWICZENIE – Iterowanie stringa.

for litera in 'abecadło':
   print(litera)
print('Jesteśmy poza pętlą.') # <- Wyświetli się, kiedy obiekt iterowalny się skończy.



# ĆWICZENIE 3 – Iterowanie stringa + instrukcje.

for litera in 'abecadło':
    if litera == 'a': # W taki sposób nie wydrukujemy literek "a"
        continue
    print(litera)

# Instrukcje "continue", "pass" i "break" mają ważność także w pętli "for".