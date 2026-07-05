####### Generowanie sekwencji liczb całkowitych z zakresu (np. 1, 2, 3, 4 w jednym obiekcie)
#
### SPOSÓB 1 – Tworzenie LISTY przy pomocy pętli "for"
#
# Jeżeli wiem, że coś ma się powtórzyć określaną liczbę razy (np. 10 razy), to jest to tak naprawdę ZAKRES.
# Jeżeli chce, żeby coś się powtórzyło 10 razy to, muszę stworzyć sekwencję 10-elementową.
# Iterując się przez nią, coś się wykona 10 razy.
#
# SKŁADNIA "range"
# "range" przyjmuje 3 argumenty: START, STOP i STEP
# range(0, 6, 2) # Wygeneruję sekwencję liczb od 0 do 10 (bez 10), co dwie.

numbers = [] # Tworzę pustą LISTĘ, która w przyszłości będzie przechowywała liczby.

zakres = range(0, 10, 2) # Tworzymy sekwencję (zakres jako LISTA)
print(zakres) # Wyświetli: range(0, 10, 2)

zakres = list(range(0, 10, 2))
print(zakres) # Wyświetli: [0, 2, 4, 6, 8]

zakres = list(range(10)) # START zawsze domyślnie wynosi 0, więc możemy zapisać: (10) – wtedy nie podajemy STEP.
print(zakres) # Wyświetli: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(0, 10, 2):
    print(i) # Wyświetli: 0 2 4 6 8
print(numbers) # ale LISTA numbers jest wciąż pusta.

for i in range(0, 10, 2):
    print(i)
    numbers.append(i) # Dodajemy zakres do LISTY.
print(numbers) # LISTA numbers jest zapełniona liczbami z zakresu [0, 2, 4, 6, 8].


### SPOSÓB 2 – LIST COMPREHENSION / wyrażenie listowe (jest to Pętla "for" zapisana w jednej linii)
#
# LIST COMPREHENSION to tak naprawdę pętla "for" zapisana w jednej linii.
# Nie musimy inicjować LISTY ani nie musimy używać ".appnend", od razy wszystko dzieje się w jednej linijce.
# Element "i", który dodaje się podczas użycia pętli "for" w ".append" znajduje się na początku wyrażenia poniżej.
# Gdybyśmy chcieli dodawać coś do LISTY i od razu powiększać o 1, to robimy to na pierwszym "i".
# List Comprehension używamy w przypadku, gdzie niewiele się dzieje (np. do przechodzenia po prostej sekwencji).
#
# SKŁADNIA List Comprehension
#
# [<modify> for <item> in <iterable> if <condition>]
# <item> to nazwa konkretnego ELEMENTU w danej iteracji
# <modify> to OPERACJA, którą chcemy wykonać na ELEMENCIE, dodając go do LISTY (możemy, ale nie musimy)
# <condition> to WARUNEK związany z <item>

my_range = [i for i in range(0, 10, 2)]
print(my_range) # Wyświetli [0, 2, 4, 6, 8]

# W List Comprehension można też dodać WARUNEK.
# Jest to bardzo popularne i używane np. do filtrowania sekwencji liczb.
#

### Czy liczbą jest parzysta?

liczba = 4

# Przy pomocy pętli "if"
if liczba % 2 == 0:
    print("Liczba jest parzysta.")
else:
    print("Liczba jest nieparzysta.")

# Przy pomocy List Comprehension
print("Liczba jest parzysta." if liczba % 2 == 0 else "Liczba jest nieparzysta.")




### FILTROWANIE z zakresu liczb – filtru tylko liczby podzielne przez 3.

numbers = []

# Przy pomocy pętli "for"
for i in range(0, 20):
    if i % 3 == 0:
        numbers.append(i)
print(numbers) # Wyświetli [0, 3, 6, 9, 12, 15, 18]

# Przy pomocy List Comprehension
my_range = [i for i in range(0, 20) if i % 3 == 0]
print(my_range) # Wyświetli [0, 3, 6, 9, 12, 15, 18]


# FILTROWANIE z zakresu liczb – filtru tylko liczby podzielne przez 3 i każdą z nich podnieś do kwadratu.

numbers = []

# Przy pomocy pętli "for"
for i in range(0, 20):
    if i % 3 == 0:
        numbers.append(i ** 2)
print(numbers) # Wyświetli [0, 9, 36, 81, 144, 225, 324]


# Przy pomocy List Comprehension
my_range = [i ** 2 for i in range(0, 20) if i % 3 == 0]
print(my_range) # Wyświetli [0, 9, 36, 81, 144, 225, 324]

# "i" znajdujące się między "for" a "in" jest filtrowane przez warunek "if i % 3 == 0".
# Następnie trafia od pierwszego "i", gdzie jest podnoszone do kwadratu "i ** 2" i dodawane do listy.