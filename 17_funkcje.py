####### FUNKCJE
#


# paradygmat proceduralny =========================================

# oblicz pole i obwod prostokątów o nastepujacych wymiarach
# 4 x 5
# 6 x 7
# 10 x 3
# 12 x 8
# 2 x 9
# wszystkie wyniki wyświetl w konsoli

# a, b = 4, 5
# area = a * b
# perimeter = 2 * (a + b)
# print(f'Prostokąt o wymiarach {a} x {b} ma pole rowne {area} j.kw oraz obwód {perimeter} j.')
#
# a, b = 6, 7
# area = a * b
# perimeter = 2 * (a + b)
# print(f'Prostokąt o wymiarach {a} x {b} ma pole rowne {area} j.kw oraz obwód {perimeter} j.')
#
# a, b = 10, 3
# area = a * b
# perimeter = 2 * (a + b)
# print(f'Prostokąt o wymiarach {a} x {b} ma pole rowne {area} j.kw oraz obwód {perimeter} j.')
#
# a, b = 12, 8
# area = a * b
# perimeter = 2 * (a + b)
# print(f'Prostokąt o wymiarach {a} x {b} ma pole rowne {area} j.kw oraz obwód {perimeter} j.')

# paradygm,ent funkcyjny =========================================
# syntax

# def func(arg1, arg2, ...):
#     function body
#     logic

def calculate_rectangle_area(edge_a: int | float, edge_b: int | float) -> float | None:
    "oblicza pole i zwraca jego wartośc, ale nie wyświetla"

    # walidacja
    if not isinstance(edge_a, (int, float)) or not isinstance(edge_b, (int, float)):
        print('krawędz musi byc typu numerycznego')
        return

    pole = edge_a * edge_b
    return pole

# def display_rectangle_area(edge_a, edge_b):
#     "oiblicza, nie zwraca jego wartości, ale wyświetla"
#     area = edge_a * edge_b
#     print(area)

# area1 = calculate_rectangle_area(10, 20) # wywołanie
# area2 = calculate_rectangle_area(3, 4) # wywołanie
#
# if area1 > area2:
#     print(f'pole 1 jest większe od pola 2 o {area1 - area2}')

# result = calculate_rectangle_area('abc', 30)
# print(result)

# napisz funckje ktora przyjie liste numerycznych i zwroci 3 wartosci - wartosc min max i dlugosc tej listy

przykladowa_lista = [1,2,3,15,74,24,54,1,86]

# print(f'min: {min(przykladowa_lista)}')
# print(f'max: {max(przykladowa_lista)}')
# print(f'dlugosc: {len(przykladowa_lista)}')

def find_list_stats(list_in: list[int | float]) -> dict[str, int | float] | None:

    for item in list_in:
        if not isinstance(item, (int, float)):
            print(f'lista musi zawierac tylko typy numeryczne, a pojawił się {item}')
            return


    return {'min': min(list_in), 'max': max(list_in), 'len': len(list_in)}

# print(find_list_stats(przykladowa_lista))

import random

# random_num = random.randint(0, 30)
# print(random_num)

list_number = []
while len(list_number) < 10:
    random_num = random.randint(0, 25)

    if random_num in list_number:
        continue

    list_number.append(random_num)

print(list_number)
print(len(list_number))








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
