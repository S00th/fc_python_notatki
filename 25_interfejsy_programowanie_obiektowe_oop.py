# Wbudowane typy i struktury danych w pythonie to wysztsko są klasy
# INTEGER, STRING, to klasy natywne (wbudowane w danym języku programowania)
# My tworząc np. nową listę, tworzymy instancję plasy list, np.

my_list1 = [1, 2, 3,4 ] # tworzę instancję klasy list
my_list2 = [11, 'Ania', True, []] # tworzę kolejną instancję

# Przechowują inne dane
# W pamięci są zapisane pod innym adresem
# ale ta sama klasa (obie są listami)

print(id(my_list1))
print(id(my_list2))

# a więc klasę możemy wdefiniować jako swego rodzaju forma na obiekt
# Jako dewoloperzy będziemy chcięli definiować własne klasy
# Wszystko pochodzi z jakiejś formy, ale indywidualną....
# Człowiek też jest klasą (każdy jest człowiekiem, ale mamy inne atrybuty)
#
# Co zawiera instancja klasy (z czego się składa)
# Każda instancja klasy
# ATRYBUTY – to cechy opisujące daną instancję (jestem instancją klasy człowiek, jestem mężczyzną, nan 1.70 m wzrostu).
# METODY – to funkcjonalności instancji (coś, co potrafi robić) – METODA to FUNKCJA zapisana w KLASIE
#

# Nazwę KLAS zaczynamy dużymi literami i PascalCase

class Person:

    print('Wykonało się.') # Instancja jest pusta i nie potrafi nic robić

person = Person() # Tworzeni instancji KLASY osoba (utworzonej przez nas klasy)
print(Person)
print(id(Person))
print(type(Person)) # <class '__main__.Person'>

# Musimy zdefiniować konstruktor

# Tworzenie DANDER metody
class Person:

    # Konstruktor / inicjalizator: ptrzyjmuje argumentu
    def __init__(self, name, age, sex):
        # Przypisujemy argumenty z konstruktora do atrybutów instancji
        self.name = name
        self.age = age
        self.age = age

    # przeciążam metodę repr, która jest odpowiedzialna na graficzną reprezentację instancji
    def __repr__(self): -> str:
        return f'Cześć, mam na imię {sefl.name} i mam {self.age} lat'

person = Person('ania', 36, 'female')

# Robimy to po to, żeby w innych miejscach mieć do stęp do atrybutów

print(person)

# Wypisz atrybuty instancji
print(person.name)
print(person.age)
print(person.sex)

# Aby to zmienić muszęprzeciązyć metodę

# __init__, __repr__, __len__ to dunder (magic) methods
# są wbudowane w każdej klasie, któa stworzymy, ale zachowuje sięw sposób domyślny
# żeby zmodyfikować ich działanie na własne potrzeby należy je nadpisać (przeciążyć) przeciążyć konstruktor
# np. repr jest odpowiedzialny za to, jak instancja jets wyświetlana

