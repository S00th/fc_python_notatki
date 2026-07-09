######## ATRYBUT PRYWATNY

class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance # Atrybut prywatny, nie ma do niego dostępu na zewnątrz, poza KLASĄ

    @propert
    def get_balance(self):
        return self.__balance

    def change_balance(self, amount):
        self.__balance += amount

bk1 = BankAccount('bk1', 100)

print(bk1.name)
print(bk1.balance)

bk1.name = 'inna nazwa'
print(bk1.name) # Poprzez operacje przypisania zmieniłem nazwę konta???

bk1.balance = 1_000_000
print(bk1.balance) # Po zabezpieczeniu atrybutu nie możemy się do niego dostać. Musimy napisać metodę, któa umożliwi
print(bk1.get.balance) # Możemy wyświetlić, ale nie zmienić. Aby zmienić, potrzebujemy kolejną metodę

bk1.change_balance(1_000)
print(bk1.change_balance)



####### DZIEDZICZENIE – jeden z najważniejszych tematów w programowaniu obiektowym
# Jedna KLASA przejmuje cechy innej KLASY

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print('Jakiś dźwięk')

# Pies dziedziczy po klasie ANIMAL.
# Dziedziczenie polega na tym, aby nie powtarzać tego samego.
class Dog(Animal):

    # Mogę przeciążyć, ale jeśli nei potrzebuje konstruktora,
    # bo jest zdefiniowany w klasie RODZICA (to po czym dziedziczymy).
    # i jeśli nie potrzebuję rozszerzać tej funkcjonoalności w konstruktorze, to nie musze jej pisać.
    def speak(self):
        print('Hau, hau')



animal1 = Animal('zwierze') # Mamy zwierze, ale jeszcze nie wiemy, co to będzie za dźwięk.
animal1.speak()
dog1 = Dog
print(dog1.name)

class Dog(Anima):

    def __init__(self, name, age):
        super().__init__(name) # Name przypisuje się z tego, co wcześniej (w Animal)

        self.age = age # A tu dopisuje to, co jeszcze ma się dziać.

dog = Dog('burek', 2)
print(dog1.name)
print(dog.age)



#######