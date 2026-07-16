####### KOMPOZYCJA
# Kompozycja to koncepcja wg. której atrybutem instancji danej klasy będzie instancja jakiejś klasy.

number = 123 # number będzie instancją klasy INTEGER
float = 1.23 # float będzie instancją klasy FLOAT
name = 'Aga' # name będzie instancją klasy STRING
# Atrybutem człowieka jest np. WIEK i sam w sobie jest liczbą, czyli instancją klasy INTEGER.



### ZADANIE
#
# Napisz prostą implementację plasy człowiek, który ma trzy atrybuty: imię, wiek, wzrost

class Human:

    def __init__(self, name: str, age: int, height: float) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.adres = adres

# Dodaj Adres, który będzie się składał z kodu pocztowego, nazwy ulicy, nazwy miasta i numeru domu
# Instancja ADDRESS musi być wcześniej

class Address:

    def __init__(self, post_code: str, street_name: str, city: str, house_number: str) -> None:
        self.post_code = post_code
        self.street_name = street_name
        self.city = city
        self.house_number = house_number

adr1 = ('01.001', 'Wroclaw', 'Czekoladowa', '12a') # Tworzymy instancję adresu

class Human:

    def __init__(self, name: str, age: int, height: float, address: Address) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.address = address # Kompozycja – atrybutem klasy człowiek jest ADRES, który jest instancją klasy Human (zagnieżdżenie).

person1 = Human('Aga', 35, 185.5, adr1) # Tworzymy instancję osoby i przypisujemy do niej adres osoby
print(person1.address.city) # Dostajemy się do konkretnego adresu: miasta (a on jets atrybutem człowieka
print(person1.address.name)

# Kod pocztowy, miasto itd. nie są bezpośrednio atrybutami instancji klasy HUMAN, tylko ADDRESS,
# ale instancja klasy ADDRESS jest atrybutem instancji klasy HUMAN.
# Na tym polega KOMPOZYCJA.

# Powyższa instancja klasy HUMAN mogłaby być zapisana jako zagnieżdżony SŁOWNIK, jak poniżej.

person1_as_dist = {
    'name': 'Grzesiek',
    'age': 35,
    'height': 185.5,
    'address': {
        'city': 'Wrocław',
        'Street': 'Czekoladowa',
        'house_number': '12a',
        'post_code': '01.001'
    }
}

# Jeśli wiemy, jak napisać słownik to po co nam klasy?
# KORZYŚCI z korzystania z implementacji własnych klas (nad zagnieżdżonym słownikiem).
# – w KLASIE kod jest bardziej uporządkowany i czysty
# – SŁOWNIK przyjmie wszystko – nieograniczona liczba pól, w klasie możemy je ograniczyć
# – W KLASIE możemy dokonać walidacji danych wejściowych, w SŁOWNIKU nie (w konstryktorze zanim...),
#   mam większą kontrolę (przykład walidacji niżej).

class Human:

    def __init__(self, name: str, age: int, height: float, address: Address) -> None:

        if not isinstance(age, (int, float)):
            raise ValueError('Age must be an integer or float') # Walidacja na typ danych
        if age < 0:
            raise ValueError('Age must be positive number') # Walidacja na znak

        self.name = name
        self.age = age
        self.height = height
        self.address = address



####### ZADANIE
#
# Dana jest implementacja klasy Point (jak niżej).
# Napisz KLASĘ Segment – odcinek.
# Odcinek to prosta, która jest ograniczona punktem początkowym i końcowym.
# Atrybutami instancji klasy Segment beda 2 punkty – start i end
# Dokonaj niezbędnej walidacji danych wejściowych

from utils.dziedziczenie_enkapsulacja import Point

class Segment:

    def __init__(self, start_point: Point, end_point: Point):

        # Sprawdzanie poprawności typów danych wejściowych
        if not isinstance(start_point, Point) or not isinstance(end_point, Point):
            raise ValueError('start_point i end_point must be a Point')

        self.start_point = start_point
        self.end_point = end_point

# Na poziomie instancji klasy Point działa walidacje z tej klasy (obie współrzędne muszą być numeryczne)
p1 = Point(1,2)
p2 = Point(3,'abc')
s1 = Segment(p1, p2) # Najpierw musimy mieć Point, żeby miec Segment



### ZADANIE
#
# Dopisz METODĘ, która sprawdzi, czy punty są takie same – z 2 takich samych punktów nie można utworzyć Segmentu.
# Walidacji zawsze dokonujemy PRZED dokonaniem przypisania

class Segment:

    def __init__(self, start_point: Point, end_point: Point):

        if not isinstance(start_point, Point) or not isinstance(end_point, Point):
            raise ValueError('start_point i end_point must be a Point')

        self.validate_coords(start_point, end_point)

        self.start_point = start_point
        self.end_point = end_point

    def validate_coords(self, p1, p2):
        if p1 == p2: # Tu korzystamy walidację, ale w...
            raise ValueError('Punkty nie mogą mieć takich samych koordynatów')



### ZADANIE
#
# Napisz metodę w klasie Segment, która wyznaczy punkt środkowy odcinka.
# Jak policzyć środek odcinka: https://www.matemaks.pl/srodek-odcinka
# Dodajemy na samy dole kodu.

    # Zaimplementowany "midpoint" może być właściwością ("@property")
    @property
    def midpoint(self):
        x = (self.start_point.x + self.end_point.x) / 2
        y = (self.start_point.y + self.end_point.y) / 2
        return Point(x, y)

    # Implementujemy metodę "move" – przesuwanie odcinka.
    # Dla uproszczenia oba punkty (początek i koniec) będą przesuwane o taki sam vektor.
    def move(self, dx, dy):
        self.start_point.move(dx, dy)
        self.end_point.move(dx, dy)

print(s1.start_point.x) # Aby dostać się do początkowego punktu x
print(s1.end_point.y) # Aby dostać się do początkowego punktu y
# Do współrzędnej musimy dostać się przez "start_point" i "end_point".

p1 = Point(-3,-1)
p2 = Point(7,6)
print(s1.midpoint)

### ZADANIE
# Jeśli chcę punky startowy odcinka s1 jako TUPLA, to muszę skorzystać z tego, co już zrobiliśmy (2 sposób).
#
# 1 sposób (NIEREKOMENDOWANY)
start_jako_tuple = (s1.start_point.x, s1.start_point.y)
print(start_jako_tuple)

# 2 sposób (REKOMENDOWANY)
print(s1.start_point.as_tuple)

print('Przed przesunięciem')
print(s1.start_point)
print(s1.end_point)

s1.move(20, 100)

print('Po przesunięciem')
print(s1.start_point)
print(s1.end_point)



### ZADANIE
#
# Zapisz w pliku
# Obiekt pythonowy "person1", który nie jest słownikiem. Jest naszym customowym typem pythonowym.
# Znajduje się w pamięci i możemy się nim posługiwać bez problemu.
# Kiedy będziemy chcieli go wysłać, to musimy go zapisać i wysłać jako plik "json".
# Musimy zamienić na słownik, słownik zserializować i zapisać dpo "json".
# Person -> dict -> jason # Serializacja dwu-etapowa

from pprint import pprint
import json

class Address:

    def __init__(self, post_code: str, street: str, city: str, house_number: str) -> None:
        self.post_code = post_code
        self.street = street
        self.city = city
        self.house_number = house_number

    def to_dict(self)
        return {
            'post_code': self.post_code,
            'city': self.city,
            'street': self.street,
            'house_number': self.house_number
        }

class Human:

    def __init__(self, name: str, age: int, height: float, address: Address) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.address = address # Kompozycja – atrybutem klasy człowiek jest ADRES, który jest instancją klasy Human (zagnieżdżenie).

    def to_dist(self)
        return {
            'name': self.name,
            'age': self.age,
            'height': self.height,
            'address': self.address.to_dict()
        }

    def save_to_json(self, filename): # Zapisanie do pliku – tworzymy METODĘ w KLASIE
        with open(filename, 'w', encoding='utf-8') as f:
            json.load(self.to.dict()), f, indent=4, ensure_asci=True)



pprint(adr1.to.dict())
pprint(person1.to_dict())
person1.save_to_json('data/json_files/person1.json')



####### ZADANIE
#
# Do istniejącej implementacji klasy Human dopisz metodę serialize, która zamienić obiekt klasy Person na jsona.

person1_as_json = json.dumps(person1_as_dict, ensure_asci=True, encoding='utf-8')

####### ZADANIE
#
# Zaimplementuj rozwiązanie oparte o poniższe 3 klasy.
# Wszystkie poniższe 3 klasy beda komponowały klasę Person w poniższy sposób.
# 1. Utwórz klasę Person z atrybutami wiek, imię i przypisz je do atrybutów instancji.
# 2. Utwórz dwie instancje klasy person.
# 3. Przeciąż metodę odpowiedzialną za wyświetlanie instancji w postaci Ania, 25 lat.
# 4. Dodaj walidację danych wejściowych: name: str, age: int
# 5. Przetestuj działanie walidacji
# Person("", 20)
# Person("Ania", -5)
# Person("Ania", "25")
# Person(123, 20)

# Person
# ├── name: str
# ├── age: int
# ├── address: Address
# ├── job: Job | None
# └── friends: list[Person]
#
# Address
# ├── postcode: str
# ├── city: str
# ├── street: str
# └── house_number: str
#
# Job
# ├── company: str
# ├── position: str
# └── salary: float

class Person:

    def init(self, name: str, age: int, address: Address) -> None:

# if isinstance(name, str) and len(name) >= 1 and age > 0: # Niezalecany sposób robienia walidacji, nie ma komunikatu
    if not isinstance(name, str) or not name.strip():
        raise TypeError('Name must be a string')
    if not isinstance(age, int) or age < 0:
        raise TypeError('Age must be a positive integer')

    self.name = name
    self.age = age
    self.address = address
    self.job = job
    self.friends = friends

    def repr(self) -> str:
        return f'Mam na imię {self.name} i mam {self.age} lat.'

p1 = Person('Aga', 20)
p2 = Person('Aga', 20)
print(p1)



####### ETAP 2
# 1. Stwórz klasę address z atrybutami: post_code, city, street, house_number
# 2. Przeciąż metodę repr w klasie, żeby wyświetlać adres w takiej formie: Floriańska 10, 31-001 Kraków
# 3. Dodaj walidacje: wszystkie pola są napisami i nie są pustymi napisami.
# 4. Do klasy Person dopisz atrybut: address, który przyjmie instancje klasy Address (dokonaj walidacji)

from utils.validators import validate_single_string_imnput

class Address:

    def __init__(self, postal_code: str, street_name: str, city: str, house_number: str) -> None:

        validate_non_empty_strings(
            postal_code=postal_code,
            city=city,
            street_name=street_name,
            house_number=house_number
        )

        self.postal_code = postal_code
        self.city = city
        self.street_name = street_name
        self.house_number = house_number

# ** kwargs - keyword arguments – podajemy argumenty po nazwie
    # Wciąż podaję nieograniczoną liczbęarguiumentów
    def validate_non_empty_string(**values) -> None:
        for name, age in value.itams():
            if not isinstance(value, str) or not value.strip():
                raise TypeError(f'Value {name} must be a non-empty string.')

    def validate_single_string_input(value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise TypeError('Value must be a non-empty string')

    def __repr__(self) -> str:
        return f"{self.street} {self.house_number}, {self.postcode} {self.city}"

        self.postal_code = postal_code
        self.street_name = street_name
        self.city = city
        self.house_number = house_number

adr1 = ('31-001', 'Kraków', 'Floriańska', '10')

class Person:

    def init(self, name: str, age: int, address: Address) -> None:

        validate_single_string_input(name)

        # if isinstance(name, str) and len(name) >= 1 and age > 0: # Niezalecany sposób robienia walidacji, nie ma komunikatu
        if not isinstance(name, str) or name == "":
            raise TypeError('Name must be a string')
        if not isinstance(age, int) or age < 0:
            raise TypeError('Age must be a positive integer')

        self.name = name
        self.age = age
        self.address = address

    def repr(self) -> str:
        return f"Cześć, mam na imię {self.name}, mam {self.age} lat."

print(p1.address.city)


####### NIE DOKOŃCZONE i wyżej też jest sporu nieład.

def give_rise(self, raise_amount):
    if isinstance(raise_amount, float):
        self.salary += raise_amount
    else:
        raise ValueError('Wpisano błędną wartość, podwyżka musi być liczbą')