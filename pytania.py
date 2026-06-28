# ####### PYTANIA itp.
#


# ####### ####### ####### Zadanie 6 – Funkcja Posortuj listę imion wg. wieku ####### ####### #######
#
#     Napisz funkcję, która jako argumenty przyjmie dwie liczby:
#     początek i koniec zakresu.
#
#     1. Zwaliduj dane wejściowe:
#         -> sprawdź, czy oba argumenty są liczbami całkowitymi,
#         -> sprawdź, czy początek zakresu nie jest większy niż koniec zakresu.
#     2. Funkcja ma za zadanie zwracać listę wszystkich liczb
#        narcystycznych z zadanego zakresu.
#
#
# -> zadanie 7
#     Gra w zgadywanie liczby.
#
#     1. Komputer losuje liczbę całkowitą z danego przedziału.
#     2. Użytkownik podaje liczbę, dopóki nie odgadnie liczby wylosowanej przez komputer.
#     3. W trakcie działania programu podpowiadaj użytkownikowi, czy podana przez niego liczba jest:
#         -> większa od wylosowanej,
#         -> mniejsza od wylosowanej.
#     4. Zliczaj liczbę prób.
#     5. Jeśli użytkownik nie odgadnie liczby w trakcie 5 prób,
#        przerwij grę i wyświetl informację o porażce.
#
#
# -> zadanie 8
#     Napisz funkcję obliczającą pierwiatki równania kwadratowego y = ax^2 + b*x + c
#
#     1. Funkcja powinna przyjmować trzy argumenty:
#         -> współczynnik a,
#         -> współczynnik b,
#         -> współczynnik c.
#     2. Rozwiąż równanie postaci:
#         -> y = ax² + bx + c
#     3. Zwaliduj dane wejściowe:
#         -> sprawdź, czy wszystkie argumenty są liczbami,
#         -> sprawdź, czy współczynnik a jest różny od 0 (wówczas mamy do czynienia z funkcja liniową a nie kwadratową)
#     4. Uwzględnij wszystkie możliwe przypadki:
#         -> brak pierwiastków rzeczywistych,
#         -> jeden pierwiastek (funkcja styczna do osi OX),
#         -> dwa różne pierwiastki.
#     5. Zwróć wynik w zależności od liczby znalezionych pierwiastków
#
#
# -> zadanie 9
#     Napisz program, który obliczy średnią:
#         -> arytmetyczną,
#         -> geometryczną,
#         -> harmoniczną
#     liczb podanych przez użytkownika.
#
#     Przy pomocy funkcji wbudowanej input pobieraj od użytkownika liczby.
#
#     Wymagania:
#         1. Waliduj dane wejściowe.
#         2. Dane nienumeryczne ignoruj, wyświetlając odpowiednią informację.
#         3. W momencie, gdy użytkownik wpisze "koniec", zakończ pobieranie danych.
#         4. Po zakończeniu wyświetl:
#             -> wynik wybranej średniej,
#             -> liczbę poprawnie pobranych wartości.
#
#
# -> zadanie 10
#     Napisz algorytm zgadywania kodu do kłódki rowerowej.
#
#     Warunki:
#         1. Kłódka jest 5-cyfrowa.
#         2. Największa możliwa do wprowadzenia cyfra to 8.
#         3. Kod nie zawiera cyfr 0 i 6.
#         4. Suma cyfr wynosi 21.
#         5. Cyfry nie powtarzają się.
#         6. Iloczyn cyfr jest większy lub równy 70.
#         7. Ostatnia cyfra jest nieparzysta.
#
#
# -> zadanie 11
#     Liczba pierwsza to taka liczba naturalna >= 2,
#     która dzieli się tylko przez 1 i samą siebie.
#
#     Napisz funkcję, która sprawdzi, czy liczba wpisana
#     przez użytkownika jest liczbą pierwszą.
#
#     Wymagania:
#         1. Zwaliduj dane wejściowe.
#         2. Funkcja powinna zwrócić informację, czy podana liczba jest liczbą pierwszą.
#
#
# -> zadanie 12
#     Liczba pierwsza to taka liczba naturalna >= 2,
#     która dzieli się tylko przez 1 i samą siebie.
#
#     Napisz program, który pobierze od użytkownika
#     początek i koniec zakresu, a następnie zwróci listę
#     wszystkich liczb pierwszych z podanego przedziału.
#
#     Wymagania:
#         1. Zwaliduj dane wejściowe.
#         2. Sprawdź, czy początek zakresu nie jest większy od końca zakresu.
#         3. Zwróć listę wszystkich liczb pierwszych należących do podanego zakresu.
#
#
# -> zadanie 13
#     Napisz funkcję, która przyjmuje tekst jako argument.
#
#     Funkcja powinna:
#         -> policzyć liczbę liter,
#         -> policzyć liczbę cyfr,
#         -> policzyć liczbę spacji,
#         -> zignorować pozostałe znaki.
#
#     Zwróć wynik w postaci słownika.
#
#
# -> zadanie 14
#     Napisz funkcję, która przyjmuje listę dowolnych elementów.
#
#     Funkcja powinna:
#         -> usunąć duplikaty,
#         -> zachować pierwotną kolejność elementów,
#         -> zwrócić nową listę.
#
#
# -> zadanie 15
#     Napisz program symulujący prosty koszyk zakupowy.
#
#     Użytkownik podaje kolejno:
#     -> nazwę produktu,
#     -> cenę produktu.
#
#     Wymagania:
#         1. Waliduj, czy cena jest liczbą dodatnią.
#         2. Pobieraj produkty do momentu wpisania "koniec".
#         3. Po zakończeniu wyświetl:
#             -> listę produktów,
#             -> łączną wartość koszyka,
#             -> najdroższy produkt.
#
#
# -> zadanie 16
#     Napisz funkcję, która sprawdzi siłę hasła.
#     Hasło uznaj za silne, jeśli:
#         -> ma co najmniej 8 znaków,
#         -> zawiera małą literę,
#         -> zawiera wielką literę,
#         -> zawiera cyfrę,
#         -> zawiera znak specjalny.
#
#     Funkcja powinna zwrócić:
#         -> True, jeśli hasło jest silne,
#         -> False, jeśli nie jest silne.
#
#
# -> zadanie 17
#     Napisz funkcję, która przyjmie dwie listy liczb.
#
#     Funkcja powinna zwrócić:
#         -> liczby występujące w obu listach,
#         -> liczby występujące tylko w pierwszej liście,
#         -> liczby występujące tylko w drugiej liście.
#
#     Wynik zwróć w postaci słownika.
#
#
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# INFORMACJA DO ZADAŃ
# twierdzenie Bézouta dla wielomianów
# Liczba a jest miejscem zerowym wielomianu W(x) wtedy i tylko wtedy, gdy reszta z dzielenia W(x) przez (x−a) jest równa 0
# https://www.matemaks.pl/twierdzenie-b%C3%A9zouta
#
# SCHEMAT HORNERA
# https://www.matemaks.pl/schemat-hornera
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
#
# -> zadanie 18
#     Napisz funkcję sprawdzającą, czy podana liczba jest miejscem zerowym wielomianu.
#
#     1. Funkcja powinna przyjmować:
#         -> listę współczynników wielomianu,
#         -> liczbę x.
#
#     2. Wielomian należy interpretować na podstawie podanych współczynników.
#
#     Przykład:
#         [2, -3, -11, 6]
#
#     oznacza:
#         2x³ - 3x² - 11x + 6
#
#     3. Oblicz wartość wielomianu dla podanej liczby x.
#     4. Wykorzystaj twierdzenie Bézouta:
#         -> jeśli wartość wielomianu wynosi 0,
#            liczba jest miejscem zerowym,
#         -> w przeciwnym przypadku nie jest miejscem zerowym.
#     5. Zwróć odpowiednią informację.
#
#
# -> zadanie 19
#     Napisz funkcję znajdującą wszystkie całkowite miejsca zerowe wielomianu.
#
#     1. Funkcja powinna przyjmować listę współczynników wielomianu.
#     2. Wyznacz wszystkie dzielniki wyrazu wolnego.
#     3. Dla każdego dzielnika sprawdź, czy jest miejscem zerowym
#        wykorzystując twierdzenie Bézouta.
#     4. Zwróć listę wszystkich znalezionych miejsc zerowych.
#
#     Przykład:
#         x³ - 6x² + 11x - 6
#
#     wynik:
#         [1, 2, 3]
#
#
# -> zadanie 20
#     Napisz funkcję realizującą schemat Hornera.
#
#     1. Funkcja powinna przyjmować:
#         -> listę współczynników wielomianu,
#         -> liczbę a.
#
#     2. Oblicz wartość wielomianu w punkcie a.
#     3. Wyznacz współczynniki wielomianu po podzieleniu przez (x - a).
#     4. Zwróć:
#         -> wartość wielomianu,
#         -> współczynniki ilorazu.
#
#     Wskazówka:
#         Jeśli wartość wielomianu wynosi 0,
#         to liczba a jest miejscem zerowym wielomianu.
#
#
# -> zadanie 21
#     Napisz program rozkładający wielomian na czynniki liniowe.
#
#     1. Program powinien przyjmować listę współczynników wielomianu.
#     2. Znajduj kolejne miejsca zerowe przy pomocy twierdzenia Bézouta.
#     3. Po znalezieniu miejsca zerowego dziel wielomian przez (x - a)
#        wykorzystując schemat Hornera.
#     4. Powtarzaj operację aż nie będzie można znaleźć kolejnych
#        całkowitych miejsc zerowych.
#     5. Wyświetl:
#         -> znalezione miejsca zerowe,
#         -> postać iloczynową wielomianu.
#
#
# -> zadanie 22
#     Napisz funkcję sprawdzającą poprawność podanych miejsc zerowych.
#
#     1. Funkcja powinna przyjmować:
#         -> listę współczynników wielomianu,
#         -> listę proponowanych miejsc zerowych.
#
#     2. Dla każdej liczby z listy:
#         -> oblicz wartość wielomianu,
#         -> wykorzystaj twierdzenie Bézouta do weryfikacji.
#
#     3. Zwróć:
#         -> listę poprawnych miejsc zerowych,
#         -> listę błędnych miejsc zerowych.
#
#
#     Przykład:
#
#     wielomian:
#         x³ - 6x² + 11x - 6
#
#     kandydaci:
#         [1, 2, 4, 5]
#
#     wynik:
#         poprawne: [1, 2]
#         błędne: [4, 5]