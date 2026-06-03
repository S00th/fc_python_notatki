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