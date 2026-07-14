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