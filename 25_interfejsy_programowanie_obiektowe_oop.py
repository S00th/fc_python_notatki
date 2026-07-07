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
        self.age = age
        # Przypisujemy po to, aby później mieć dostęp do przypisanych ATRYBUTÓW.

    # PRZECIĄŻANIE metodę repr, która jest odpowiedzialna na graficzną reprezentację instancji
    def __repr__(self) -> str:
        return f'Cześć, mam na imię {sefl.name} i mam {self.age} lat.'

person = Person('ania', 36, 'female')

print(person) # Zostanie wyświetlone zdanie po "return" kiedy KLASA zostanie przeciążona.

# Wypisz atrybuty instancji
print(person.name)
print(person.age)
print(person.sex)

# Aby to zmienić muszęprzeciązyć metodę

# __init__, __repr__, __len__ to dunder (magic) methods
# są wbudowane w każdej klasie, któa stworzymy, ale zachowuje sięw sposób domyślny
# żeby zmodyfikować ich działanie na własne potrzeby należy je nadpisać (przeciążyć) przeciążyć konstruktor
# np. repr jest odpowiedzialny za to, jak instancja jets wyświetlana





class BloodBowlPlayer:

    def __init__(self, team, position, cost, skills):
        self.team = team
        self.position = position
        self.cost = cost
        self.skills = skills

    def __repr__(self) -> str:
        return f'Twoim ulubionym pozycyjnym jest {self.position} o koszczie {self.cost} g.'

human_blitzer = BloodBowlPlayer('Human', 'Blitzer', 85_000, ['Block', 'Tackle', 'Dodge'])

print(human_blitzer.team)
print(human_blitzer.position)
print(human_blitzer.cost)
print(human_blitzer.skills)
print(human_blitzer) # Wyświetli zdanie po "return" jeżeli KLASA zostanie PRZECIĄŻONA