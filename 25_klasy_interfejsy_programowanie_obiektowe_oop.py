# Wbudowane TYPY i STRUKTURY danych w pythonie – to wszystko to są klasy.
# INTEGER, STRING, to KLASY natywne (wbudowane w danym języku programowania).
# My jako devoloperzy czy analitycy danych będziemy chcieli na własne potrzeby tworzyć własne KLASY,
# tworząc np. nową listę, tworzymy INSTANCJĘ KLASY LISTA, np.

my_list1 = [1, 2, 3,4 ] # tworzę instancję klasy LISTA
my_list2 = [11, 1.23, 'Ania', True, []] # tworzę kolejną instancję

# Przechowują różne dane.
# W pamięci są zapisane pod innym adresem/w różnych miejscach (dwie różne instancje),
print(id(my_list1))
print(id(my_list2))
# ale ta sama KLASA (obie są LISTAMI).

# A więc KLASĘ możemy zdefiniować jako swego rodzaju FORMĘ na OBIEKT (jak forma na ciasto).
# Człowiek też jest klasą (każdy jest człowiekiem, ale mamy inne atrybuty)

# Co zawiera instancja KLASY (z czego się składa?)
# Każda instancja KLASY (np. człowiek może zostać opisany imieniem, nazwiskiem, wagą itp.) posiada:
# – ATRYBUTY – to cechy opisujące daną instancję (jestem instancją klasy CZŁOWIEK, mężczyzną, man 170 cm wzrostu).
# – METODY – to funkcjonalności instancji (coś, co potrafi robić) – METODA, to FUNKCJA zapisana w KLASIE.
# Nazwę KLAS zapisujemy w PascalCase (pierwsze słowo zaczyna się od wielkiej litery, łączy kilka słów w jeden ciąg
# bez spacji i zaczynają każde kolejne słowo wielką literą).

class Person:

    print('Wykonało się.')  # Instancja jest pusta (nie przechowuje żadnej informacji) i nie potrafi nic robić


person = Person()  # Tworzeni instancji KLASY osoba (utworzonej przez nas KLASY)
print(Person)  # Wyświetli: <class '__main__.Person'>
print(id(Person))  # Wyświetli: 2413146306528
print(type(Person))  # Wyświetli: <class '__main__.Person'>


# Żeby nadać jakieś ATRYBUTY nowo utworzonej KLASIE, musimy zdefiniować KONSTRUKTOR (przy pomocy METODY "__init__").
# Jest to tzw. tworzenie DANDER metody.
# Jeżeli definiujemy METODĘ, to każda KLASA w Pythonie pozwala nadpisać DANDER metodę.

class Person:

    # KONSTRUKTOR/INICJALIZATOR: przyjmuje ARGUMENTY (name, age, sex)
    def __init__(self, name, age, sex):
        # Przypisujemy argumenty z KONSTRUKTORA do ATRYBUTÓW instancji
        self.name = name
        self.age = age
        self.sex = sex
        # Przypisujemy po to, aby później mieć dostęp do przypisanych ATRYBUTÓW.

    # Wcześniej konstruktor "__init__" zadziałał w domyślny sposób, ponieważ utworzył się konstruktor plasy "person",
    # ale chce, aby konstruktor utworzył instancję w pamięci i żeby też przypisał atrybuty (aby obiekt przechowywał informacje).
    # Dlatego trzeba przeciążyć konstruktor.
    # PRZECIĄŻANIE metodę (wbudowaną) "repr", która jest odpowiedzialna na graficzną reprezentację instancji.
    def __repr__(self) -> str:
        return f'Cześć, mam na imię {self.name} i mam {self.age} lat.'

    # METODA instancji (będzie wywoływana na instancji)
    def drive(self):
        return 'Driving ...'

person = Person('ania', 36, 'female')

print(person) # Zostanie wyświetlone zdanie po "return" kiedy KLASA zostanie przeciążona.

# Wypisz atrybuty instancji
print(person.name)
print(person.age)
print(person.sex)

# Aby to zmienić, muszę PRZECIĄŻYĆ metodę.

# Dunder (magic) methods: __init__, __repr__, __len__, __getitem__
# Są wbudowane w każdej klasie, którą stworzymy, ale zachowuje się w sposób domyślny.
# Żeby zmodyfikować ich działanie na własne potrzeby, należy je nadpisać (przeciążyć) – przeciążyć KONSTRUKTOR,
# np. "__repr__" jest odpowiedzialny za to, jak instancja jest wyświetlana.

### ZADANIE
# Do istniejącej klasy Person dopisz taka funkcjonalność, która zwróci rok urodzenia danej osoby.



### Przykład z BB

# class BloodBowlPlayer:
#
#     def __init__(self, team, position, cost, skills):
#         self.team = team
#         self.position = position
#         self.cost = cost
#         self.skills = skills
#
#     def __repr__(self) -> str:
#         return f'Twoim ulubionym pozycyjnym jest {self.position} o koszczie {self.cost} g.'
#
# human_blitzer = BloodBowlPlayer('Human', 'Blitzer', 85_000, ['Block', 'Tackle', 'Dodge'])
#
# print(human_blitzer.team)
# print(human_blitzer.position)
# print(human_blitzer.cost)
# print(human_blitzer.skills)
# print(human_blitzer) # Wyświetli zdanie po "return" jeżeli KLASA zostanie PRZECIĄŻONA



### ZADANIE
# Do istniejącej klasy Person dopisz taka funkcjonalność, która zwróci rok urodzenia danej osoby.

from datetime import date

class Person:

    # ATRYBUTY KLASY – cechy/wartości wspólne dla każdego człowieka (tworzymy pod nazwą klasy, przed konstruktorem).
    CURRENT_YEAR = date.today().year
    GENRE = 'homo sapiens'

    def __init__(self, name, age, sex, bank_balance):
        self.name = name
        self.age = age
        self.sex = sex
        self.bank_balance = bank_balance

    def __repr__(self) -> str:
        return f'Cześć, mam na imię {self.name} i mam {self.age} lat.'

    # ... bierzemy ze świata zewnętrznego.
    # METODA instancji przyjmuje argumenty (dane z zewnątrz), jest wywoływana na instancji klasy.
    def earn(self, amount: int) -> None :
        self.bank_balance += amount
        print(f'Zarobiłeś {amount} zł, twój aktualny stan konta to: {self.bank_balance}')

    # Funkcjonalności tego typu powinny być napisane jako WŁAŚCIWOŚCI (dekorator)
    # WŁAŚCIWOŚĆ (@property) to taka specjalna METODA, która nie potrzebuje informacji z zewnątrz, zatem nie będzie potrzebowała ARUMENU
    # Działa jedynie na danych z wewnątrz INSTANCJI.
    # Wywołuje się ją jak ATRYBUT (jak tu: imię, wiek, płeć).
    @property
    def get_birthyear(self):
        # return date.today().year - self.age
        return self.CURRENT_YEAR - self.age

    # FABRYKA OBIEKTÓW. Będzie wywoływane na klasie
    @classmethod
    def create_default_person(cls):
        return cls('Jan', '50', 'M', 10_000)

person = Person('ania', 36, 'female', 1_000) # Tworzenie instancji klasy osoba

print(person) # Zostanie wyświetlone zdanie po "return" kiedy KLASA zostanie przeciążona.

# Wypisz atrybuty instancji
print(person.name)
print(person.age)
print(person.sex)
print(person.earn(100))
print(person.bank_balance)
print(date.today().year)
print(person.get_birthyear)

default_person = Person.create_default_person()
print(default_person)



### PRZYKŁAD – kalkulator funkcyjne

# def sum(a :{__add__}), b):
#     return a + b
#
# def sub(a :{__sum__}), b):
#     return a - b
#
# def mul(a :{__mul__}), b):
#     return a * b
#
# def div(a :{__truediv__}), b):
#     try:
#         return a / b
#     expect ZeroDivisionError as e:
#         print('zero division is not allowed')
#
# usage_odomiter = 0
# usage_odomiter2 = 0
# x, y - 5, 8
#
# sum(x, y)
# usage_odometer += 1
# sub(x, y)
# usage_odometer += 1
# sum(x, y)
# usage_odometer += 1
# mul(x, y)
# usage_odometer += 1
# print(usage_odometer)
#
# mul(x, y)
# sum(x, y)
# usage_odometer2 += 1

class Calculator:

    usage_odometer = 0 # Definiujemy ATRYBUT KLASY (chociaż bardziej jest to ATRYBUT INSTANCJI)
    # Kupując nowy kalkulator, ma na liczniku zero obliczeń.

    def __init__(self, brand: str, price: float) -> None:
        self.brand = brand
        self.price = price

    # Przeciążamy metodę i definiujemy jak ma się zachowywać
    def __gt__(self, other) -> bool:
        return self.usage_odometer >= other.usage_odometer # Porównywane jest zużycie kalkulatorów.
                                                           # Wystarczy przeciążyć jedną z METOD.

    def sum(self, a :{__add__}, b):
        self.usage_odometer =+ 1
        return a + b

    def sub(self, a :{__sum__}, b):
        self.usage_odometer = + 1
        return a - b

    def mul(self, a :{__mul__}, b):
        self.usage_odometer = + 1
        return a * b

    def div(self, a :{__truediv__}, b):
        self.usage_odometer = + 1
        try:
            return a / b
        except ZeroDivisionError as e:
            print('Zero division is not allowed')

calc1 = Calculator('Casio', 130)

print(calc1.sum(10, 20)) # Wywołujemy METODY
print(calc1.usage_odometer)
print(calc1.sum(10, 20))
print(calc1.sum(10, 20))
print(calc1.sum(10, 20))
print(calc1.sum(10, 20))
print(calc1.usage_odometer)

calc2 = Calculator('Vector', 40)
print('Zużycie kalkulatora 1: ', calc1.usage_odometer)
print('Zużycie kalkulatora 2: ', calc2.usage_odometer)

print(calc1 > calc2) # Wyświetli Type Error, ale jeśli przeciążymy metodę
print(calc1 == calc2)



### ZADANIE
# Do obecnej implementacji klasy Calculator dopisz funkcjonalność baterii.
# Za każdą operacją, poziom baterii będzie spadać o 1%.

class Calculator:

    usage_odometer = 0 # Definiujemy ATRYBUT KLASY (chociaż bardziej jest to ATRYBUT INSTANCJI)
    # Kupując nowy kalkulator, ma na liczniku zero obliczeń.

    def __init__(self, brand: str, price: float) -> None:
        self.brand = brand
        self.price = price
        self.battery_level = 100

    # Przeciążamy metodę i definiujemy jak ma się zachowywać
    def __gt__(self, other) -> bool:
        return self.usage_odometer >= other.usage_odometer # Porównywane jest zużycie kalkulatorów.
                                                           # Wystarczy przeciążyć jedną z METOD.

    def sum(self, a :{__add__}, b):
        self.usage_odometer =+ 1
        self.battery_level -= 1
        return a + b

    def sub(self, a :{__sum__}, b):
        self.usage_odometer = + 1
        self.battery_level -= 1
        return a - b

    def mul(self, a :{__mul__}, b):
        self.usage_odometer = + 1
        self.battery_level -= 1
        return a * b

    def div(self, a :{__truediv__}, b):
        self.usage_odometer = + 1
        self.battery_level -= 1
        try:
            return a / b
        except ZeroDivisionError as e:
            print('Zero division is not allowed')

calc1 = Calculator('Casio', 130)

print(calc1.sum(10, 20)) # Wywołujemy METODY
print(calc1.usage_odometer)
print(calc1.sum(10, 20))
print(calc1.sum(10, 20))
print(calc1.sum(10, 20))
print(calc1.sum(10, 20))
print(calc1.usage_odometer)

calc2 = Calculator('Vector', 40)
print('Zużycie kalkulatora 1: ', calc1.usage_odometer)
print('Zużycie kalkulatora 2: ', calc2.usage_odometer)

print(calc1 > calc2) # Wyświetli Type Error, ale jeśli przeciążymy metodę
print(calc1 == calc2)


#### Wersja bez powtarzania dodawania zużycia baterii

class Calculator:
    usage_odometer = 0  # Definiujemy ATRYBUT KLASY (chociaż bardziej jest to ATRYBUT INSTANCJI)

    # Kupując nowy kalkulator, ma na liczniku zero obliczeń.

    def __init__(self, brand: str, price: float) -> None:
        self.brand = brand
        self.price = price
        self.battery_level = 100

    # Przeciążamy metodę i definiujemy jak ma się zachowywać
    def __gt__(self, other) -> bool:
        return self.usage_odometer >= other.usage_odometer  # Porównywane jest zużycie kalkulatorów.
        # Wystarczy przeciążyć jedną z METOD.

    @property
    def _update_device(self): # Metoda chroniona. Podkreślenie informuje "nie wywołuj poza..."
        self.usage_odometer = + 1
        self.battery_level -= 1
        return self.usage_odometer, self.battery_level

    def sum(self, a: {__add__}, b):
        self._update_device
        return a + b

    def sub(self, a: {__sum__}, b):
        self._update_device
        return a - b

    def mul(self, a: {__mul__}, b):
        self._update_device
        return a * b

    def div(self, a: {__truediv__}, b):
        self._update_device
        try:
            return a / b
        except ZeroDivisionError as e:
            print('Zero division is not allowed')


calc1 = Calculator('Casio', 130)

print(calc1.sum(10, 20))  # Wywołujemy METODY
print(calc1.usage_odometer)
print(calc1.sum(10, 20))
print(calc1.sum(10, 20))
print(calc1.sum(10, 20))
print(calc1.sum(10, 20))
print(calc1.usage_odometer)

calc2 = Calculator('Vector', 40)
print('Zużycie kalkulatora 1: ', calc1.usage_odometer)
print('Zużycie kalkulatora 2: ', calc2.usage_odometer)

print(calc1 > calc2)  # Wyświetli Type Error, ale jeśli przeciążymy metodę
print(calc1 == calc2)


### ZADANIE
#
# ĆWICZENIE
# Uprość kod zastępując cztery metody do obliczeń arytmetycznych jedną.
# Dodaj dodatkowy argument, dzięki któremu będzie wiadomo, jaka operacja ma zostać wykonana.
# Dokonaj niezbędnych walidacji.
# Zachowaj oryginalną funkcjonalność kalkulatora (zdolność wykonywania operacji arytmetycznych,
# aktualizacja poziomu baterii i licznika użyć)
# Nową metodę nazwij calculate


class Calculator:
    usage_odometer = 0  # Definiujemy ATRYBUT KLASY (chociaż bardziej jest to ATRYBUT INSTANCJI)

    # Kupując nowy kalkulator, ma na liczniku zero obliczeń.

    def __init__(self, brand: str, price: float) -> None:
        self.brand = brand
        self.price = price
        self.battery_level = 100

    # Przeciążamy metodę i definiujemy jak ma się zachowywać
    def __gt__(self, other) -> bool:
        return self.usage_odometer >= other.usage_odometer  # Porównywane jest zużycie kalkulatorów.
        # Wystarczy przeciążyć jedną z METOD.

    @property
    def _update_device(self): # Metoda chroniona. Podkreślenie informuje "nie wywołuj poza..."
        self.usage_odometer = + 1
        self.battery_level -= 1
        return self.usage_odometer, self.battery_level

    def sum(self, a: {__add__}, b):
        self._update_device
        return a + b

    def sub(self, a: {__sum__}, b):
        self._update_device
        return a - b

    def mul(self, a: {__mul__}, b):
        self._update_device
        return a * b

    def div(self, a: {__truediv__}, b):
        self._update_device
        try:
            return a / b
        except ZeroDivisionError as e:
            print('Zero division is not allowed')

    def calculate(self, a, b, operation):
        pass

typ_operacji = 'dodaj'
a, b = 10, 4

# if operacja == 'dodaj':
#     print(a + b)
# elif operacja == 'odejmij':
#     print(a - b)
# elif operacja == 'mnożenie':
#     print(a * b)
# elif operacja == 'dzielenie':
#     print(a / b)
# else:
#     print('Nie ma takiej operacji')
#
# print(operacja.get(operacja, 'Nie ma takiej operacji'))

# Zamiast jak wyżej lepiej dać SŁOWNIK jak niżej.

operacja = {
    'sum': a + b,
    'sub': a - b,
    'mul': a * b,
    'div': a / b,
}

# Nie ma nic szybszego niż mapping. Jeśli mamy duży wybór

# Możemy też zrobić to tak (FUNKCJE anonimowe zapisane w SŁOWNIKU):
operacja = {
    'sum': lambda x :{__add__}, y: x + y,
    'sub': lambda x :{__sub__}, y: x - y,
    'mul': lambda x :{__mul__}, y: x * y,
    'div': lambda x :{__ne__}, x / y if y !=0 else None
}

dzialanie = operacja.get(typ_operacji)

print(dzialanie(10, 5))



#######

class Calculator:
    usage_odometer = 0

    def __init__(self, brand: str, price: float) -> None:
        self.brand = brand
        self.price = price
        self.battery_level = 100

    def __gt__(self, other) -> bool:
        return self.usage_odometer >= other.usage_odometer

    @property
    def _update_device(self):
        self.usage_odometer = + 1
        self.battery_level -= 1
        return self.usage_odometer, self.battery_level

    def calculate(self, a, b, op_type):

        self._update_device()

        operations = {
            'sum': lambda x: {__add__}, y: x + y,
            'sub': lambda x: {__sub__}, y: x - y,
            'mul': lambda x: {__mul__}, y: x * y
            'div': lambda x: {__ne__}, x / y if y != 0 else None
        }

        func = operations.get(op_type)
        if func is None:
            print('Unknown operation')
            return
        result = func(a, b)
        if result is None:
            print('ZeroDivision Error')
            return
        return result


###### GEOM

import math

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __reor__(self):
        return f'Point ({self.x}, {self.x})'

    def distance(self, pt) -> float:
        return math.dist((self.x, self.y), (pt.x, pt.y))

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1.distance(p2))


### Kod Daniela

# import math
#
# class Point:
#     # __init__ to konstruktor
#     def __init__(self, x:int | float, y: int | float):
#         self.x = x
#         self.y = y
#
#
#     # za pomocą @property i metody setter mogę wykonać walidacje wejścia
#
#     @property # (getter) pobieramy dane
#     def x(self): # x przekierowujemy do _x, od teraz x i _x są ze sobą połączone, _x
#         return self._x # _x to pusta przestrzeń, do której zostanie przypisana wartość, jeśli setter ją sprawdzi i wszystko będzie ok
#     # (setter) modifikujemy / filtrujemy dane
#     @x.setter # wywołuje metodę setter, czyli "bramkarza" który sprawdza x z property, jeśli spełnia wymagania to przypisuje wartość do _x, jeśli nie to podnosi błąd.
#     def x(self, value):
#         if not isinstance(value, (int,float)): # sprawdzamy value X
#             raise TypeError("Współrzędna x musi być typu int lub float!")
#         self._x = value # jeśli wszystko jest ok, to do _x zostaje przypisana wartość wejścia usera
#
#     @property
#     def y(self):
#         return self._y
#
#     @y.setter
#     def y(self, value):
#         if not isinstance(value, (int,float)):
#             raise TypeError("Współrzędna y musi być typu int lub float!")
#         self._y = value
#
#     def __repr__(self):
#         # _x i x są połączone, ale wedle zasad, nie wywołujemy rzeczy z podkreślikiem
#         return f'POINT ({self.x}, {self.y})'
#
#     def distance(self, pt):
#             return float(math.dist((self.x, self.y), (pt.x, pt.y)))

###


### ZADANIE
# Do aktualnej implementacji klasy point dopisz niezbędne walidacje wejścia
# Napisz metodę klasy from_iterable - która utworzy instancję klasy Point z obiektu iterowalnego 1D (z tupli, listy)

#######

import math

class Point:
    # __init__ to konstruktor
    def __init__(self, x:int | float, y: int | float):
        self.validate_xy_coords(x, y) # Walidacja w konstruktorze przed...
        self.x = x
        self.y = y

    def __repr__(self, pt: {dist, x, y}) -> float:
        return math.distance((self.x, self.y), (pt.x, pt.y))

    def __add__(self, other :(x, y)):
        if not isinstance(other, Point):
            reise TypeError('Object has not type of Point')
        return Point(self.x + other.x, self.y + other.y)

    def distance(self, pt):
        return float(math.dist((self.x, self.y), (pt.x, pt.y)))

    def validate_is_point(self, pt):
    if not isinstance(pt, Point):
        return TypeError('Object has not type of Point')

        # Metoda statyczna wprawdzie jest zdefiniowana z KLASIE,
    # ale konwencjonalnie, koncepcyjnie i logicznie nie jest ściśle związana z klasą,
    # mogłaby być równie dobrze odrębną FUNKCJĄ.
    # Nie ma SELF.

    @staticmethod
    def validate_xy_cords(x, y) -> None:

        if not isinstance(x, (float, int)) or not isinstance(y, (float, int)):
            raise TypeError('Both x and y has to be of numeric type')

    # ???
    @classmethod
    def from_iterable(cls, iterable):
        if len(iterable) != 2:
            raise TypeError('Iterable must be of lenght equals ro 2')
        x, y = iterable # rozpakowujemy obiekt iterowalny
        return cls(x, y)

    @property
    def as_tuple(self):
        return self.x, self.y

    @property
    def as_list(self):
        return[self.x, self.y]

    @property
    def distance_from_origin(self):
        return math.dist((0, 0), self.as_tuple)

    # Enkapsulacja ograniczanie dostępu.
    # Wskazówka, żeby nei wywoływać ten metody na zewnątrz, tylko wewnątrz klasy.
    # W pododny sposób możemy ograniczyć dostęp do atrybutów.
    def _protested(self):
        return 'Chroniona'

    def _private(self):
        return 'private'


p1 = Point(1, 2)
p2 = Point(3, 4.5)

my_tuple = (10, 23)
#           x   y

p3 = Point(my_tuple[0], my_tuple[1])
p4 = Point.from_iterable(my_tuple)
p5 = Point.from_iterable([4, 9]) # tutaj LISTA, ale nie ważne czy lista, czy coś innego.

print('p3', p3)
print('p4', p4)
print('p5', p5)

print(p1.as_tuple)


### GEOMETRIA ANALITYCZNA – nie moja bajka :)
#



####### Metody magiczne


# Enkapsulacja ograniczanie dostępu (do obiektów).
# Wskazówka, żeby nei wywoływać ten metody na zewnątrz, tylko wewnątrz klasy.
# W podobny sposób możemy ograniczyć dostęp do atrybutów.
# Nie wszystko powinno byćdostępne na zewnątrz
def _protested(self):
    return 'Chroniona'

# Nie da się jej wywołaćna zewnątrz
def _private(self):
    return 'private'

print()