####### FUNKCJE
#

przykladowa_lista = [1, 2, 3, 15, 74, 24, 54, 1, 86, 5]

print(f'min: {min(przykladowa_lista)}')
print(f'max: {max(przykladowa_lista)}')
print(f'dlugosc: {len(przykladowa_lista)}')


# # def calculate_rectangle_area(edge_a: int | float, edge_b: int | float) -> float | None:
# #
# #     if not isinstance(edge_a, (int, float)) or (edge_b, (int, float)):
# #         print('krawędz musi byc typu numerycznego')
# #         return
# #     pole = edge_a * edge_b
# #     return pole
# #
# # result = calculate_rectangle_area(10, 30)
# # print(result)
#
#
# przykladowa_lista = [1, 2, 3, 15, 74, 24, 54, 1, 86, 5]
#
# print(f'min: {min(przykladowa_lista)}')
# print(f'max: {max(przykladowa_lista)}')
# print(f'dlugosc: {len(przykladowa_lista)}')
#
#
# def paint_list_stats(list_in: list[int | float])
#     return min(list_in), max(list_in), len(list_in)
#
# # lub
#
# def func(przykladowa_lista):
#     list_len = len(przykladowa_lista)
#     min_value = min(przykladowa_lista)
#     max_value = max(przykladowa_lista)
#     return min_value, max_value, list_len
# print(f'min: {min(przykladowa_lista)}')
# print(f'max: {max(przykladowa_lista)}')
# print(f'dlugosc: {len(przykladowa_lista)}')
#
#
# def find_list_stats(list_in: list[int | float]) -> dict[str, int | float]:
#     return {'min': min(list_in), 'max': max(list_in), 'len': len(list_in)}
#
# print(find_list_stats(przykladowa_lista))


# random_num = random.randint(0, 30)
# print(random_num)

# utwórz listę 10 liczb pseudolosowych z przedziału od 0 do 100


import random

list_number = []

for number in range(10):
    list_number.append(random.randint(0, 25))
    if number != number:
