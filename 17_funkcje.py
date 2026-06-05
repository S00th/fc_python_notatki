####### FUNKCJE

# FUNKCJA to wydzielony, nazwany fragment kodu, który wykonuje określone zadanie.
# FUNKCJE piszemy po to, aby uniknąć powtarzania kodu. Nie musimy pisać tych samych instrukcji wielokrotnie.
# Inaczej mówiąc, jeżeli jakieś działania cały czas się powtarzają, FUNKCJE pozwalają użyć wielokrotnie tego samego fragmentu kodu.
# FUNKCJA będzie czymś w rodzaju szablonu dla kodu.
# FUNKCJE zwiększają czytelność, zmniejszają ilość kodu oraz ułatwiają rozwiązanie skomplikowanych problemów

# SKŁADNIA
def <nazwa_funkcji>():
    kod

# W chwili kiedy FUNKCJA jest ZDEFINIOWANA (ma już nazwę) i zostały dodane jakieś INSTRUKCJE, jeszcze NIC SIĘ NIE DZIEJE.
# Aby FUNKCJA zadziałała (została WYWOŁANA) musimy odnieść się do FUNKCJI przez jej nazwę.
# Żeby WYWOŁAĆ FUNKCJĘ, trzeba napisać jej nazwę, otworzyć i zamknąć nawias, a pomiędzy nawiasami wpisać wartości ARGUMENTÓW.
# WAŻNE! FUNKCJĘ trzeba stworzyć przed WYWOŁANIEM funkcji
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

# Tutaj znajduje się DEFINICJA funkcji (czyli logika, która ma zajść).
def func(arg1, arg2):
    function body # We WCIĘCIU mamy CIAŁO FUNKCJI...
    logic # oraz logikę, która zachodzi w FUNKCJI

print(func(arg1, arg2)) # Tutaj znajduje się wywołanie funkcji



### WARTOŚĆ ZWRACANA / Zwracanie wartości FUNKCJI
#
# ZWRACANIE WARTOŚĆ to proces, w którym funkcja PRZESYŁA WYNIK swojej pracy z powrotem do miejsca,
# z którego została WYWOŁANA (inaczej mówiąc: FUNKCJA przejmuje dane WEJŚCIOWE, PRZETWARZA je i zwraca dane WYJŚCIOWE).
# Wynik działania FUNKCJI nie „znika” po jej zakończeniu.
# Wynik można np. przypisać do zmiennej i wykorzystać w dalszej części kodu, np. do kolejnych obliczeń lub jako warunek w instrukcji "if".
# FUNKCJA może zwrócić jeden lub wiele obiektów (zwraca coś dzięki "return"), ale NIE musi nic zwracać.
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
#
# SCOPE to zmienne zdefiniowanych wewnątrz funkcji.
# Są one widoczne tylko dla tej konkretnej funkcji i przestają istnieć po zakończeniu jej wykonywania.

def obwod_prostokata1(a, b):
    obwod = 2 * (a + b) # Zmienne a i b istnieją wewnątrz FUNKCJI, ale nie dysponujemy nimi na zewnątrz (znajdują się w tzw. SCOPEie FUNKCJI).
    return obwod

# lub – krótszy zapis

def obwod_prostokata2(a, b):
    return 2 * (a + b) # Przypisanie WARTOŚCI następuje niżej (poza FUNKCJĄ)

obwod1 = obwod_prostokata1(2, 2)
obwod2 = obwod_prostokata1(2, 5)
obwod3 = obwod_prostokata1(2, 10)

print(obwod1)
print(obwod2)
print(obwod3)

### WAŻNE

liczba = 10

def dodaj(a, b):
    return a + liczba

result = dodaj(5, 7)

print(result) # Wyświetli 15, ponieważ "liczba" została przypisana przed FUNKCJĄ na sztywno.
                # "a" nie należy do SCOPE całego kodu, ale "liczba" może być w SCOPE FUNKCJI ("b" nie jest wykorzystywane).



### Typowanie wartości / Podpowiadanie typów (Type hinting)

def calculate_area(edge_a, edge_b):
    area = edge_a * edge_b
    return area

area = calculate_area('Aga', 20) # Jeżeli spróbuje dodać dwie różne wartości (STR i INT)... to zwróci nam 20 razy powtórzone Aga.
print(area) # Wyświetli AgaAgaAgaAgaAgaAgaAgaAgaAgaAgaAgaAgaAgaAgaAgaAgaAgaAgaAgaAga

# W takim przypadku musimy sprawdzić wartości wejściowe, czyli zWALIDOWAĆ dane wejściowe.
# Tworząc FUNKCJĘ, zazwyczaj będziemy chcieli OTYPOWAĆ zmienne (jak niżej).
# Typowanie wartości / Podpowiadanie typów (Type hinting) nie obliguje nas do niczego. To jedynie info dla nas, że tutaj powinien być np. INT.
# Pozwalająca na jawne określenie, jakiego rodzaju dane powinny być przechowywane w zmiennych lub przetwarzane przez funkcje.
# WAŻNE! Podpowiadanie TYPÓW jest dziś pożądaną praktyką.

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



### ĆWICZENIE – Liczba narcystyczna (liczba Armstronga)
#
# Napisz funkcję, która przyjmuje na wejściu liczbę naturalną i sprawdza, czy liczba jest narcystyczna.
# Liczba narcystyczna to liczba naturalna, która jest równa sumie swoich cyfr podniesionych do potęgi równej liczbie cyfr w liczbie.
# Inaczej
# Liczba narcystyczna to liczba naturalna, której suma cyfr podniesionych do potęgi długości tej liczby, to wartość tej liczby,
# np. 153 - 1³ + 5³ + 3³ to 153 – do potęgi trzeciej po są trzy cyfry (np: 153, 370, 1634).
#  liczby naturalne, które są równe sumie swoich cyfr podniesionych do potęgi równej liczbie cyfr w liczbie.
# wykładnik (eng. exponent)
# number = str(153)
# print(len(number)) # W ten sposób wyciągamy długość liczby. Długość liczby jest nam potrzebna do wykładnika potęgi.

# W pierwszym FUNKCJI jedynie informujemy, że WARTOŚĆ znajdująca się tutaj powinna być typu INT (jest opcjonalne). Prawdziwa WALIDACJA odbywa się niżej.
def liczba_narcystyczna(number: int) -> bool:
    if not isinstance(number, int): # Tutaj odbywa się prawdziwa WALIDACJA wejścia. Jeżeli liczba nie jest INT, to chcemy wyjść z FUNKCJI i celowo podnieść BŁĄD.
        raise TypeError('Liczba musi być całkowita.') # Podnosimy BŁĄD – tutaj jest tylko informacją o tym, że w samej funkcji (linia 264)
    str_number = str(number)  # Przypisujemy zmienna, która nam się przyda do kilku rzeczy.
    exponent = len(str_number) # Określamy exponent (wykładnik potęgi), aby mieć dynamicznie przypisany (zmienny) exponent.
    cum_sum = 0 # Suma, która się kumuluje
    for digit in str_number:
        cum_sum += int(digit)**exponent
    return cum_sum == number # Nie ma potrzeby pisać tutaj "if" ponieważ tutaj i tak otrzymujemy bool.

number = int(input('Podaj liczbę: '))
if liczba_narcystyczna(number):
    print(f'Liczba {number} jest narcystyczna.')
else:
    print(f'Liczba {number} NIE jest narcystyczna.')



####### W Pythonie można definiować FUNKCJE na różne sposoby.
#
# Najczęściej korzystamy z "def", w których będzie się wykonywała jakaś logika.
# W przypadku bardzo prostej FUNKCJI, która nir wymaga kilku linii, możemy ją napisać w jednej linijce prz pomocy FUNKCJI ANONIMOWEJ lambda.
# FUNKCJA ANONIMOWA / lambda jest rzadko używana, ale warto wiedzieć, że coś takiego istnieje.
#
# SKŁADNIA
# lambda <argument_1>, <argument_2>: <co_ma_się_stać_z_argumentami>

suma1 = lambda x, y: x + y

# Jest to dokładnie to samo co:

def suma2(x, y):
    return x + y

print(suma1(2, 3))
print(suma2(2, 3))



######## ĆWICZENIE – SORTOWANIE znaków w LIŚCIE

# Każdy symbol ma swoją wartość numeryczną wg. tabeli ASCII.
letters = ['a', 'Z', '?', 'w', 'B', 'y', 'a', '#']

# W przypadku wyrazów brana jets pod uwagę pierwszy znak, jeśli byłby taki sam, to drugi.
names = ['Basia', 'Danusia', 'Katarzyna', 'Ola', 'Małgorzata']

sorted_letters = sorted(letters) # Funkcja "sorted" sortuje obiekt KOLEKCJI. Zawsze zwraca LISTĘ w kolejności wg. ASCII.
print(sorted_letters)



######## ĆWICZENIE – Posortuj LISTĘ imion wg. długości imienia
#

names = ['Katarzyna', 'Basia', 'Danusia', 'Ola', 'Małgorzata']

print(sorted(names, key=len)) # W argumencie "key" wpisujemy jakiej FUNKCJI, która ma pomóc w porównywaniu.



######## ĆWICZENIE – Posortuj LISTĘ tupli wg. wieku osób.
# Lista w tupli jest przykładem OBIEKT DWU-WYMIAROWEGO.

people = [('Basia', 23), ('Ania', 19), ('Kasia', 27), ('Ola', 21)]
# inny zapis
people = [
    ('Basia', 23),
    ('Ania', 19),
    ('Kasia', 27),
    ('Ola', 21)
]

# for wiek in people:
#     print(wiek[1]) # Dla każdego elementu LISTY wyciągamy element 1.

print(sorted(people, key=lambda x: x[-1])) # Gdzie x będzie każdym elementem wewnętrznym w LIŚCIE tupli. Tu wyciągamy ostatni element z każdej tupli.
print(sorted(people, key=lambda x: x[-1], reverse=True)) # Gdybyśmy chcieli odwrócić kolejność LISTY, dodajemy "reverse=True".
print(sorted(people, key=lambda x: x[-1])[::-1]) # Inny sposób odwracania kolejności LISTY. Zwraca listę w odwrotnej kolejności.



####### MODÓŁ "import string"
#
import string # MODUŁ, który zwraca wszystkie znaki.

print(string.ascii_letters) # Zwróci wszystkie litery: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_lowercase) # Zwróci wszystkie małę litery: abcdefghijklmnopqrstuvwxyz
print(string.ascii_uppercase) # Zwróci wszystkie DUŻE litery: ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits) # Zwróci wszystkie litery: 0123456789
print(string.punctuation) # Zwróci wszystkie znaki specjalne: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~


####### ZADANIE DOMOWE
#
# Dany jest moduł "strip.
# Zbuduj funkcję do generowania haseł.
# Funkcja powinna przyjmować następujące argumenty:
# – Żądana długość hasłą (funkcja umożliwia podanie żądanej długości hasłą – w agrumentach).
# – Czy zawrzeć znaki specjalne, jeśli True to zawrzyj, jeśli False to nie zawieraj.
# – No końcu wymieszaj litery.
# Otypuj argumenty, wartości zwracane. Dokonaj niezbędnej walidacji wejścia.








### DOWOLNA liczba ARGUMENTÓW – *args
#
# def dodaj_trzy(num_1, num_2, num_3): # Nie dodajemy wielu argumentów w ten sposób.
#     return num_1 + num_2 + num_3
#
# def dodaj_trzy(num_1, num_2, num_3): # Nie dodajemy wielu argumentów w ten sposób.
#     return num_1 + num_2 + num_2
#
# result = dodaj_trzy(1, 2)
#
# Jeżeli mamy z góry określoną liczbę argumentów POZYCYJNYCH, to wywołanie funkcji z inną ilością (mniejszą lub większą), spowoduje błąd.
# ARGUMENT POZYCYJNY to taki argument, który nie ma wartości domyślnej.
#
# "*" przed nazwą argumentu liczby pełni rolę OPERATORA PAKOWANIA ARGUMENTÓW POZYCYJNYCH (tzw. *args).
# Pozwala on na wywołanie FUNKCJI z dowolną liczbą wartości przekazanych po przecinku.
# Nie musisz z góry określać, czy będziesz dodawać dwie, trzy czy sto liczb.
# Wszystkie wartości przekazane podczas wywołania FUNKCJI zostają SPAKOWANE do jednej struktury danych – TUPLI o nazwie "liczby".
# Wewnątrz funkcji możesz operować na niej jak na zwykłej kolekcji danych.

def dodaj_wiele(*liczby):
    return sum(liczby)

result = dodaj_wiele(1, 2, 3, 100, 200) # Mogę tutaj wpisać dowolną ilość wartości
print(result)



####### ROZPAKOWYWANIE
#
# SKŁADNIE – jest odwrotna niż przy przypisywaniu wartości
# <wartość1>, <wartość2>, <wartość2> = <nazwa>

# def rozpakuj(*names):
#     return names

names = ['Zosia', 'Ania', 'Kasia']
name1, name2, name3 = names # W takim przypadku liczba zmiennych musi być dokładnie taka sama jak zmiennych w LIŚCIE.
print(name1, name2, name3)

names = ['Zosia', 'Ania', 'Kasia', 'Tomek']
name1, name2, name3, _ = names # Dodany "_" to konwencja, która mówi "Wiemy, że coś tu jest, rozpakowujemy to, ale nie będziemy do tego zaglądali.
print(name1, name2, name3)
print(_) # DO "_" w tym przypadku jest przypisany "Tomek"

names = ['Zosia', 'Ania', 'Kasia', 'Tomek', 'Janek', 'Leszek']
name1, name2, name3, *_ = names # "*_" rozpakuje skumulowaną dynamiczną liczbę wartości w kolekcji
print(name1, name2, name3) # Wyświetli: Zosia, Ania, Kasia i zignoruje wszystkie pozostałe imiona, które nas nie interesują.



####### ARGUMENT POZYCYJNY i OPCJONALNY
#
# Czasem chcemy podawać cześć argumentów jako zawsze inna, a cześć jako zawsze takie same.
# ARGUMENT POZYCYJNY to taki argument, który NIE ma wartości domyślnej – jest sugestią (wartość domyślną wpisuje się w momencie definiowania funkcji).
# ARGUMENT OPCJONALNY to taki argument, który ma wartość domyślną. Pozwalają zdefiniować FUNKCJĘ, aby niektóre parametry miały przypisaną wartość.
#       Jeśli podczas wywoływania funkcji pominiesz ten argument, to Python automatycznie użyje przypisanej mu wartości.

# Podczas definiowania FUNKCJI została wpisana WARTOŚĆ DOMYŚLNA dla "pi" (sugestia).
# "radius" jest argumentem pozycyjnym, a "pi" argumentem opcjonalnym.
def circle_area(radius: int | float, pi: float = 3.14):
    print(f' {radius=}, {pi=}') # Tak zapis pomaga w debugowaniu. Zaciągnie WARTOŚCI i wyświetli: radius=2, pi=3.14
    return pi * radius ** 2 # Gdybyśmy w tym miejscu zamiast "pi" wpisali 3.14, byłaby to wartość wpisana "na sztywno"

circle_area1 = circle_area(2) # Mimo tego, że nie podaliśmy drugiego argumentu, FUNKCJA wykonała obliczenie
circle_area2 = circle_area(2, 3.1425932) # Tutaj zostanie NADPISANA wartość ARGUMENTU OPCJONALNEGO (priorytetem jest to, co wpiszemy w WYWOŁANIU).

print(circle_area1)
print(circle_area2)

# WAŻNA! Jeżeli używasz w FUNKCJI zarówno argumentó POZYCYJNYCH i OPCJONALNYCH, to w DEFINICJI FUNKCJI, argumenty POZYCYJNE muszą być pierwsze.
def circle_area(pi: float = 3.14, radius: int | float): # WAŻNE! Taki zapis podniesie BŁĄD SKŁADNI.
    print(f' {radius=}, {pi=}')
    return pi * radius ** 2



### ARGUMENT POZYCYJNY, *args i ARGUMENT OPCJONALNY

def oblicz_wydatki(name: str, *wydatki, last_name: str = 'Nowak') -> float | int:
    print(f'Witaj {name} {last_name}. ')
    suma_wydatkow = sum(wydatki)
    print(f'Twoje wydatki to {wydatki}')
    return suma_wydatkow

oblicz_wydatki('Aga', 1, 5, 10, 500) # Zostaną zaciągnięte odpowiednie wartości.
oblicz_wydatki('Aga', 1, 5, 10, 500, last_name='Kowalska') # Na końcu musimy wskazać argument OPCJONALNY.



#### ĆWICZENIE
# Napisz FUNKCJĘ, która przyjmie dowolną liczbę elementów.
# Wyodrębnij z niej LICZBY CAŁKOWITE.
# POGRUPUJ odpowiednio i zwróć LICZBY PARZYSTE i NIEPARZYSTE jako osobne LISTY.
# Zignoruj wejścia inne niż INTEGER.

# ETAP 1

def split_odds_even(*args: int):
    print(args) # Informacyjnie: sprawdzamy, czym są "args". Wyświetli nam zawartość args: (1, 2, 3, 4, 5)
    print(type(args))  # Sprawdzamy typ danych: tuple

split_odds_even(1, 2, 3, 4, 5)


# ETAP 2

def split_odds_even(*args: int):
    even_numbers = [] # Tworzymy LISTĘ liczb parzystych, aby przechować liczby, które będziemy dodawać w pętli.
    odd_numbers = [] # Tworzymy LISTĘ liczb nieparzystych
    for item in args:
        if item % 2 == 0: # Sprawdzanie parzystości liczby
            even_numbers.append(item) # Dodajemy do LISTY liczby parzyste
        else:
            odd_numbers.append(item) # Dodajemy do LISTY liczby nieparzyste
    print(even_numbers)
    print(odd_numbers)

split_odds_even(1, 2, 3, 4, 5, 6, 7, 8, 9)

# W tym momencie FUNKCJA jeszcze nic nie zwraca.


# ETAP 3

def split_odds_even(*args: int):
    even_numbers = []
    odd_numbers = []
    for item in args:
        if not isinstance(item, int): # Jeżeli element args nie jest liczbą całkowitą, to nie rób nic i przejdź do kolejnego elementu.
            continue
        if item % 2 == 0:
            even_numbers.append(item)
        else:
            odd_numbers.append(item)
    print(even_numbers)
    print(odd_numbers)

split_odds_even(1, 2, 3, 4, 5, 6, 7, 8, 9, 'Aga') # Jeśli dodamy do listy stringa.


# ETAP 4

def split_odds_even(*args: int):
    even_numbers = []
    odd_numbers = []
    for item in args:
        if not isinstance(item, int): # Jeżeli element args nie jest liczbą całkowitą, to nie rón nic i przejdź do kolejnego elementu.
            continue
        if item % 2 == 0:
            even_numbers.append(item)
        else:
            odd_numbers.append(item)
    print(even_numbers)
    print(odd_numbers)
    return even_numbers, odd_numbers

split_odds_even(1, 2, 3, 4, 5, 6, 7, 8, 9, 'Aga', 3.14) # Jeśli dodamy do listy stringa.
