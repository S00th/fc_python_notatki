import random
#
# lista = []
# max_len = 10 # Chcę 10 liczb w liście
# start_range = 1
# end_range = 20
# while len(lista) < max_len: # Sprawdza, czy w LISTA (jej zawartość) jest mniejsza niż 10 (przy 10 skończy się wykonywać)
#     random_num = random.randint(start_range,end_range)
#     if random_num not in lista: # Zanim dodamy liczbę do LISTY, sprawdzamy, czy liczba jest już na LIŚCIE.
#         lista.append(random_num) # w przeciwnym wypadku nie jest potrzebne.
# print(lista)
# print(len(lista))



def get_random_numbers(start_range: int, end_range: int, out_len: int) -> list[int]:
    if out_len > (end_range - start_range) + 1: # Aby zapobiec sytuacji, w której ZAKRES +1 jest większy niż DŁUGOŚĆ
        raise ValueError(f'Out_len={out_len} is out of range')
    numbers_list = []
    while len(numbers_list) < out_len:
        num = random.randint(start_range, end_range)
        if num not in numbers_list:
            numbers_list.append(num)
    return numbers_list
zmienna = get_random_numbers(1,20,5)

print(zmienna)
print(len(zmienna))
