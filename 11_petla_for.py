####### PĘTLA FOR
#
# Pętli FOR używamy tam, gdzie mamy do czynienia z pewnym OGRANICZONYM ZBIOREM, przez który chcemy przejść.
# ZAKOŃCZY SIĘ w momencie, kiedy skończy się ZBIÓR DANYCH (kiedy zakończy się obiekt ITEROWALNY).
# Przykładem obiektu iterowalnego jest zakres liczb lub STRING – ponieważ słowo możemy przeliterować.
# bool, int i float nie są obiektami iterowalnymi.


### SKŁADNIA
#
# for <tymczasowa_zmienna> in <obiekt_iterowalny>:>
    # kod wewnątrz pętli <blok kodu>

# for <- słowo kluczowe.
# <tymczasowa_zmienna> <- żyje tylko w momencie pętli "for".
# Kiedy będziemy ITEROWALI tą zmienną, to przy każdej kolejnej ITERACJI pętli "for" będzie przyjmowała wartość kolejnego elementu zbioru danych.
# in <- słowo kluczowe.
# <obiekt_iterowalny> <- zmienna STRING, ZAKRES LICZB lub STRUKTURA DANYCH.



# ĆWICZENIE 1 – Przez jakie liczby jest podzielna podana liczba?

nasza_liczba = int(input('Podaj swoją liczbę: '))

for liczba in range(1, nasza_liczba):
    if nasza_liczba % liczba == 0:
        print(f'{nasza_liczba} jest podzielna przez {liczba}]')
    # if nasza_liczba % 3 == 0:
    #     print('Liczba jest podzielna przez 3')

# renge() <- ITERATOR, a nie funkcja, ale chwilowo traktujemy go jak funkcję ;)
# w nawiasie podajemy: range(<zakres_początkowy>, <zakres końcowy>)



# ĆWICZENIE 2 – Iterowanie stringa.

for litera in 'abecadło':
   print(litera)
print('Jesteśmy poza pętlą.') # <- Wyświetli się, kiedy obiekt iterowalny się skończy.



# ĆWICZENIE 3 – Iterowanie stringa + instrukcje.

for litera in 'abecadło':
    if litera == 'a': # W taki sposób nie wydrukujemy literek "a"
        continue
    print(litera)

# Instrukcje "continue", "pass" i "break" mają ważność także w pętli "for".