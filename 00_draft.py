from datetime import date

class Person:

    def __init__(self, name, age, sex, bank_balance):
        self.name = name
        self.age = age
        self.sex = sex
        self.bank_balance = bank_balance

    def __repr__(self) -> str:
        return f'Cześć, mam na imię {self.name} i mam {self.age} lat.'

    # ... bierzemy ze świata zewnętrznego.
    def earn(self, amount: int) -> None :
        self.bank_balance += amount
        print(f'Zarobiłeś {amount} zł, twój aktualny stan konta to: {self.bank_balance}')

    # Funkcjonalności tego typu powinny być napisane jako WŁAŚCIWOŚCI (dekorator)
    # WŁAŚCIWOŚĆ to taka specjalna METODA, która nie potrzebuje informacji z zewnątrz, zatem nie będzie potrzebowała ARUMENU
    # Działa jedynie na danych z wewnątrz INSTANCJI.
    # Wywołuje się ją jak ATRYBUT (jak tu: imię, wiek, płeć).
    @property
    def get_birthyear(self):
        return date.today().year - self.age

person = Person('ania', 36, 'female', 1_000)

print(person) # Zostanie wyświetlone zdanie po "return" kiedy KLASA zostanie przeciążona.

# Wypisz atrybuty instancji
print(person.name)
print(person.age)
print(person.sex)
print(person.earn(100))
print(person.bank_balance)
print(date.today().year)
print(person.get_birthyear)
