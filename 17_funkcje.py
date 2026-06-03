####### FUNKCJE

# FUNKCJE piszemy po to, aby uniknąć powtarzania kodu. Nie musimy pisać tych samych instrukcji wielokrotnie.
# Inaczej mówiąc, jeżeli jakieś działania cały czas się powtarzają, FUNKCJE pozwalają użyć wielokrotnie tego samego fragmentu kodu.
# FUNKCJA będzie czymś w rodzaju szablonu dla kodu.
# FUNKCJE zwiększają czytelność, zmniejszają ilość kodu oraz ułatwiają rozwiązanie skomplikowanych problemów

# SKŁADNIA
def <nazwa_funkcji>():
    kod

# W chwili kiedy FUNKCJA jest zdefiniowana (ma już nazwę) i zostały dodane jakieś INSTRUKCJE, jeszcze nic się nie dzieje.
# Aby FUNKCJA zadziałała (została wywołana) musimy odnieść się do FUNKCJI przez jej nazwę.
#
# WAŻNE, aby FUNKCJĘ stworzyć przed jej WYWOŁANIEM
#
nazwa # w tym momencie jest to zmienna
nazwa() # w tym momencie jest to funkcja


####### PARADYGMAT proceduralny
# Paradygmat proceduralny opiera się na organizowaniu kodu wokół procedur, które w języku Python są nazywane FUNKCJAMI.
# W tym podejściu program jest traktowany jako ciąg instrukcji wykonywanych krok po kroku,
# gdzie złożone zadania dzieli się na mniejsze, dające się zarządzać fragmenty (jak w przykłądzie niżej).

# Oblicz pole i obwód prostokątów o następujących wymiarach:
# 4 x 5
# 6 x 7
# 10 x 3
# 12 x 8
# 2 x 9
# Wszystkie wyniki wyświetl w konsoli

# a, b = 4, 5
# area = a * b
# perimeter = 2 * (a + b)
# print(f'Prostokąt o wymiarach {a} x {b} ma pole równe {area} j.kw oraz obwód {perimeter} j.')
#
# a, b = 6, 7
# area = a * b
# perimeter = 2 * (a + b)
# print(f'Prostokąt o wymiarach {a} x {b} ma pole równe {area} j.kw oraz obwód {perimeter} j.')
#
# a, b = 10, 3
# area = a * b
# perimeter = 2 * (a + b)
# print(f'Prostokąt o wymiarach {a} x {b} ma pole równe {area} j.kw oraz obwód {perimeter} j.')
#
# a, b = 12, 8
# area = a * b
# perimeter = 2 * (a + b)
# print(f'Prostokąt o wymiarach {a} x {b} ma pole równe {area} j.kw oraz obwód {perimeter} j.')

# PARADYGMAT, ent funkcyjny =========================================



### SKŁADNIA
# Argumentami (arg1, arg 2) będą dane, które będą potrzebne do wykonania obliczenia/zadania

def func(arg1, arg2, ...):
    function body # We WCIĘCIU mamy CIAŁO FUNKCJI...
    logic # oraz logikę, która zachodzi w FUNKCJI



### ZWRACANIE WARTOŚĆ FUNKCJI
#
# ZWRACANIE WARTOŚĆ to proces, w którym funkcja przesyła wynik swojej pracy z powrotem do miejsca,
# z którego została wywołana (można powiedzieć, że przejmuje dane wejściowe, przetwarza je i zwraca dane wyjściowe).
# Wynik działania FUNKCJI nie „znika” po jej zakończeniu.
# Wynik można np. przypisać do zmiennej i wykorzystać w dalszej części kodu, np. do kolejnych obliczeń lub jako warunek w instrukcji "if".
#
# Wyobraź sobie, że prosisz małżonka (FUNKCJĘ) o zrobienie zakupów.
# Dajesz mu listę zakupów i pieniądze (ARGUMENTY).
# Małżonek (FUNKCJA) wykonuje pracę i przynosi Ci (ZWRACA) zakupy.
# Możesz teraz schować je do lodówki (zapisać w ZMIENNEJ) lub
# wykorzystać jako składnik obiadu (wykonać kolejną FUNKCJĘ).

def calculate_area(edge_a, edge_b):
    # FUNKCJA oblicza i ZWRACA wartość, ale nie WYŚWIETLA wartości
    area = edge_a * edge_b # area "żyje" w pamięci do tego momentu. Jeśli NIE wyjdziemy z FUNKCJI (użyjemy "return"), to WARTOŚĆ zostanie zapisana w pamięci)
    return area # Tutaj ma miejsce jedynie funkcjonalność

def display_area(edge_a, edge_b):
    # FUNKCJA oblicza i WYŚWIETLA wartość, ale bez słowa kluczowego return nie ZWRACA wartości
    area = edge_a * edge_b # area "żyje" w pamięci do tego momentu. Jeśli wyjdziemy z FUNKCJI (NIE użyjemy "return"), to WARTOŚĆ przestanie istnieć (nie każda FUNKCJA musi coś zwracać)
    print(area)

area = calculate_area(10, 20) # Tutaj WYWOŁUJEMY FUNKCJĘ, a WARTOŚĆ zostaje PRZYPISANA (o ile wcześniej została ZWRÓCONA)
# Jeżeli nie przypiszę WARTOŚCI, to WARTOŚĆ zniknie
print(area) # Wyświetli 200

area2 = display_area(10, 20)
print(area2) # Wyświetli 200 i "None" – bez słowa kluczowego "return" FUNKCJA nic nie zwróci (zostało przypisane "None")

area1 = calculate_area(10, 20)
area2 = calculate_area(3, 4)

if area1 > area2:
    print(f'Pole 1 jest większe od pola 2 o {area1 - area2}') # Mogę wykorzystać FUNKCJĘ do porównania pola dwóch kwadratów.
    # Gdybym chciał wykorzystać "display_area", to otrzymam błąd, bo FUNKCJA zwróciła "None".



### ĆWICZENIE 1 – Oblicz obwód prostokąta

def obwod_prostokata1(a, b):
    obwod = 2 * (a + b)
    return obwod

# lub – krótszy zapis

def obwod_prostokata2(a, b):
    return 2 * (a + b) # Przypisanie WARTOŚCI następuje niżej

obwod1 = obwod_prostokata1(2, 2)
obwod2 = obwod_prostokata1(2, 5)
obwod3 = obwod_prostokata1(2, 10)

print(obwod1)
print(obwod2)
print(obwod3)



### Typowanie wartości / Podpowiadanie typów (Type hinting)

def calculate_area(edge_a, edge_b):
    area = edge_a * edge_b
    return area

area = calculate_area('Aga', 20) # Jeżeli spróbuje dodać dwie różne wartości (STR i INT)... to zwróci nam 20 razy powtórzone Aga.
print(area) # Wyświetli AgaAgaAgaAgaAgaAgaAgaAgaAgaAgaAgaAgaAgaAgaAgaAgaAgaAgaAgaAga

# W takim przypadku musimy sprawdzić wartości wejściowe, czyli zWALIDOWAĆ dane wejściowe.
# Tworząc FUNKCJĘ, zazwyczaj będziemy chcieli OTYPOWAĆ zmienne (jak niżej).
# Typowanie wartości / Podpowiadanie typów (Type hinting) nie obliguje nas do niczego.
# Pozwalająca na jawne określenie, jakiego rodzaju dane powinny być przechowywane w zmiennych lub przetwarzane przez funkcje.

def calculate_area(edge_a: int | float, edge_b: int | float) -> float | None:
    # TYPOWANIE FUNKCJI: WARTOŚĆ edge_a - edge_b spodziewam się INT lub FLOAT, a FUNKCJA zwróci FLOAT lub None
    # Inaczej mówiąc (<argument_1>: <jakiego typu> lub <jakiego typu>, <argument_2>: <jakiego typu> lub <jakiego typu>) -> <co_zwraca>
    # WALIDACJA
    area = edge_a * edge_b
    return area

area = calculate_area('Aga', 20)
print(area)



### WALIDACJA w FUNKCJI

# Jeżeli chcielibyśmy zatrzymać wykonywanie FUNKCJI, musimy zrobić WALIDACJE w FUNKCJI – zanim się ona wykona (dzięki temu będzie napisana tylko raz).

def calculate_area(edge_a: int | float, edge_b: int | float) -> float | None:
    if not isinstance(edge_a, (int, float)) or not isinstance(edge_b, (int, float)): # Tutaj odbywa się WALIDACJA danych wejściowych.
        # Jeśli dane wejściowe są ok (są typami numerycznymi), to zostanie wykonana FUNKCJA.
        # isinstance(value, class) - Sprawdza czy dana WARTOŚĆ jest danego typu (klasy) i zwraca BOOL
        print('Krawędź musi byc typu numerycznego.') # Jeśli dane wejściowe NIE są typami numerycznymi), to FUNKCJA NIE zostanie wykonana.
        return # W przypadku WARTOŚCI nienumerycznych, pojawi się tutaj jakby return "None i zostanie zwrócone "None".
    area = edge_a * edge_b
    return area

area1 = calculate_area('Aga', 20)
area2 = calculate_area(2, 20)
area3 = calculate_area(5, 20)
print(area) # W przypadku WARTOŚCI nienumerycznych (jak wyżej) wyświetli None.
print(area)
print(area)



### ĆWICZENIE
#
# Napisz funkcję, która przyjmie listę numerycznych i zwróci trzy WARTOŚCI: wartość min, wartość max i długość listy.

def find_list_stats(list_in: list[int | float]) -> int | float:
    return min(list_in), max(list_in), len(list_in) # Jeżeli zwracamy więcej niż jedną wartość, to wypisujemy po przecinku.

przykladowa_lista = [1,2,3,15,74,24,54,1,86]

print(find_list_stats(przykladowa_lista)) # W Zwróci i wyświetli TUPLE: (1, 86, 9)


# Jeśli chcielibyśmy, aby zwrócony został SŁOWNIK:

def find_list_stats(list_in: list[int | float]) -> int | float:
    return {'min': min(list_in), 'max': max(list_in), 'lenght': len(list_in)}

przykladowa_lista = [1,2,3,15,74,24,54,1,86]

print(find_list_stats(przykladowa_lista)) # W Zwróci i wyświetli SŁOWNIK: {'min': 1, 'max': 86, 'lenght': 9}


# Jeżeli chcielibyśmy ZWALIDOWAĆ dane wejściowe (wiemy, że jedna z wartości w liście jest STR),
# musimy przeiterować się przez listę.

def find_list_stats(list_in: list[int | float]) -> float | None:
    for item in list_in:
        if not isinstance(item, (int, float)): # Wystarczy, że jedne element nie jest int lub float
            print(f'Lista musi zawierać tylko typy numeryczne, a pojawił się {item}.')
            return
    return {'min': min(list_in), 'max': max(list_in), 'lenght': len(list_in)} # Jeżeli zwracamy więcej niż jedną wartość, to wypisujemy po przecinku.

przykladowa_lista = [1,2,3,15,74,24,54,1,'TEKST']

print(find_list_stats(przykladowa_lista))



### ĆWICZENIE – Utwórz listę 10 losowych liczb
# Utwórz listę 10 losowych liczb pseudo losowych z przedziału 0-100. Liczby mogą się powtarzać.

import random

list_num = []

for num in range(10): #
    list_num.append(random.randint(0, 20)) # Utwórz listę składająca się z 10 liczb z przedziału od 0 do 20

print(list_num)



### ĆWICZENIE – Utwórz listę 10 LOSOWYCH liczb
# Utwórz listę 10 losowych liczb pseudo losowych z przedziału 0-100. Liczby mogą się powtarzać.
# Liczby nie mogą się powtarzać

import random

list_num = []

for num in range(10): #
    random_num = random.randint(0, 20)
    if random_num in list_num: # Sprawdza, czy liczba jest już w liście.
        continue
    list_num.append(random_num)

print(list_num)
print(len(list_num))

# Niestety wynikiem takiej Funkcji będzie LISTA, która czasem będzie miała mniej niż 10 liczb.
# Aby temu zapobiec, musimy skorzystać z pętli "while" – sprawdzić długość listy (zapętlić az będzie, się składałą z 10 liczb)

while len(list_num) < 10:
    random_num = random.randint(0, 20)
    if random_num in list_num:
        continue
    list_num.append(random_num)

print(list_num)
print(len(list_num))








przykladowa_lista = [1, 2, 3, 15, 74, 24, 54, 1, 86, 5]

print(f'min: {min(przykladowa_lista)}')
print(f'max: {max(przykladowa_lista)}')
print(f'dlugosc: {len(przykladowa_lista)}')


# # def calculate_rectangle_area(edge_a: int | float, edge_b: int | float) -> float | None:
# #
# #     if not isinstance(edge_a, (int, float)) or (edge_b, (int, float)):
# #         print('krawędz musi byc typu numerycznego')
# #         return
# #     pole = edge_a * edge_b
# #     return pole
# #
# # result = calculate_rectangle_area(10, 30)
# # print(result)
#
#
# przykladowa_lista = [1, 2, 3, 15, 74, 24, 54, 1, 86, 5]
#
# print(f'min: {min(przykladowa_lista)}')
# print(f'max: {max(przykladowa_lista)}')
# print(f'dlugosc: {len(przykladowa_lista)}')
#
#
# def paint_list_stats(list_in: list[int | float])
#     return min(list_in), max(list_in), len(list_in)
#
# # lub
#
# def func(przykladowa_lista):
#     list_len = len(przykladowa_lista)
#     min_value = min(przykladowa_lista)
#     max_value = max(przykladowa_lista)
#     return min_value, max_value, list_len
# print(f'min: {min(przykladowa_lista)}')
# print(f'max: {max(przykladowa_lista)}')
# print(f'dlugosc: {len(przykladowa_lista)}')
#
#
# def find_list_stats(list_in: list[int | float]) -> dict[str, int | float]:
#     return {'min': min(list_in), 'max': max(list_in), 'len': len(list_in)}
#
# print(find_list_stats(przykladowa_lista))


# random_num = random.randint(0, 30)
# print(random_num)

# utwórz listę 10 liczb pseudolosowych z przedziału od 0 do 100


import random

list_number = []

for number in range(10):
    list_number.append(random.randint(0, 25))
    if number != number:

        # napisz, która przyjmie dowolną liczbe elementów, wyodreąbnij z niej liczby całkowite,
        # pogrupuj odpowiednio i zwróc liczby parzyste jakos osobna lista i niepatrzyste w osobnej liscie,
        # zignoruj wejścia inne niz integer

        # def slit_odds_even(*args: int | float):
        #     even_numbers = []
        #     odd_numbers = []
        #     for arg in args:
        #         if arg % 2 == 0:
        #             even_numbers.append(arg)
        #     for arg in args:
        #         if arg % 2 == 1:
        #            odd_numbers.append(arg)

        # Etap 1
        # def slit_odds_even(*args: int | float):
        #     print(args)
        #     print(type(args))
        #
        # slit_odds_even(1,2,3,4,5)

        # Etap 2
        # def slit_odds_even(*args: int | float):
        #     for item in args:
        #         print(item)
        #         if item % 2 == 0:
        #             print('Liczby są parzyste')
        #                     else:
        #             print
        # slit_odds_even(1,2,3,4,5)

        # Etap 3
        # def slit_odds_even(*args):
        #     even_numbers = []
        #     odd_numbers = []
        #     for item in args:
        #         if item % 2 == 0:
        #             even_numbers.append(item)
        #         else:
        #             odd_numbers.append(item)
        #     print(even_numbers)
        #     print(odd_numbers)
        #
        # slit_odds_even(1,2,3,4,5)

        # Etap 4 a - zbłędem
        # def slit_odds_even(*args):
        #     even_numbers = []
        #     odd_numbers = []
        #     for item in args:
        #         if item % 2 == 0:
        #             even_numbers.append(item)
        #         else:
        #             odd_numbers.append(item)
        #     print(even_numbers)
        #     print(odd_numbers)
        #
        # slit_odds_even(1,2,3,4,5 '1,b,c,d,e,f,') # tutaj nie można sprawdzić napisu czy jets parzysty czy nie

        # Etap 4 b
        def slit_odds_even(*args):
            even_numbers = []
            odd_numbers = []
            for item in args:
                if not isinstance(item,
                                  int):  # Jeżeli element args nie jets liczbą całkowitą to nie rób nic i przejdź do kolejnego elementu
                    continue
                if item % 2 == 0:
                    even_numbers.append(item)
                else:
                    odd_numbers.append(item)
            print(even_numbers)
            print(odd_numbers)


        slit_odds_even(1, 2, 3, 4, 5, '1,b,c,d,e,f,', 3.14, True, None)  # tym zmiennych nie ma już znaczenia