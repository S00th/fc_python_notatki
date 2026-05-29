####### OBIEKTY
#


####### DRAFT
#

####### ĆWICZENIE – SLOTY. Dodaj film na serwer
# Funkcja któa przyjmuje na wejsciu liczbę

# suma_mb_filmow = 0
# ilosc_slotow = 1 # Utworze przynajmniej 1 slot więc zaczynam od 1, a nie od 0.
# max_wielkosc_slotu = 10_000
# aktualna_wielkosc_slotu = 0
# najlzejszy_slot = 1
# wielkosc_najlzejszego_slotu = 10_000
# najciezszy_slot = 0
#
# ilosc_filmow = int(input('Ile filmów chcesz dodać na serwer? '))
#
# for ilosc_filmow in range(ilosc_filmow): # Zapis: range(ilosc_filmow), jest tożsamy z: range(0, ilosc_filmow)
#     rozmiar_filmu = float(input('Podaj rozmiar filmu: '))
#     if 100 > rozmiar_filmu > 3_000: # Jeżeli film będzie mniejszy niż 100 MB lub większy niż 3000 MB...
#         break # Przerwij
#     suma_mb_filmow += rozmiar_filmu
#     if rozmiar_filmu + aktualna_wielkosc_slotu <= max_wielkosc_slotu: # Jeżeli spełniony jest ten warunek...
#         aktualna_wielkosc_slotu += rozmiar_filmu # To dodaje tą wartość.
#     else: # A jeżeli nie...
#         if aktualna_wielkosc_slotu < wielkosc_najlzejszego_slotu: # Na rozmiar slotu patrzę w momencie, kiedy skończę ładować do niego dane.
#             najlzejszy_slot = ilosc_slotow # Ilość slotów mówi nam też, na którym slocie aktualnie jesteśmy (można ją jakby przypisać do drugiej rzeczy).
#             wielkosc_najlzejszego_slotu = aktualna_wielkosc_slotu # Po to, żebyśmy mieli slot, który ma 8_000, a nie 10_000.
#         aktualna_wielkosc_slotu = ilosc_filmow # Zamykam slot...
#         ilosc_slotow += 1 # i dodaje nowy film do poprzedniego.
# print()
# print(f'Całkowity rozmiar filmów: {suma_mb_filmow} MB')
# print(f'Ilość wykorzystanych slotów: {ilosc_slotow}')
# print(f'Pusta przestrzeń dyskowa: {ilosc_slotow * max_wielkosc_slotu - suma_mb_filmow} MB')
# print(f'Najlżejszy slot, to slot {najlzejszy_slot} z dostępną pojemnością {wielkosc_najlzejszego_slotu}')
#
# # Do zrobienia jest jeszcze jedno sprawdzenie, które już jest w tym kodzie:
#
# # if 100 > rozmiar_filmu > 3_000:  # Jeżeli film będzie mniejszy niż 100 MB lub większy niż 3000 MB...
# #     break  # Przerwij
# # suma_mb_filmow += rozmiar_filmu
# # if rozmiar_filmu + aktualna_wielkosc_slotu <= max_wielkosc_slotu:  # Jeżeli spełniony jest ten warunek...
# #     aktualna_wielkosc_slotu += rozmiar_filmu  # To dodaje tą wartość.
#
#
# a = int(input('Podaj liczbę 1: '))
# b = int(input('Podaj liczbę 2: '))
# c = int(input('Podaj liczbę 3: '))
# potega = int(input('Podaj potęgę: '))
#
# 1^3 + 5 ^3 _ 3 ^ 3 = 153
#
# (a ** x) + (b ** x) + (c ** x) = abc
# #
#
#
# def is_arms_num(num: int) -> bool:
#     if not isinstance(num, int):
#         raise TypeError('num must be an integer')
#     str_num = str(num)
#     exponent=len(str(str_num))
#     for digit in str_num:
#     for num in numbers:
#         plus = num + 1



# names = ['Ania', 'Gosia', 'Katarzyna', 'Anna', 'Ola']
# print(sorted(names, key=len))



# Posortuj listę tupli wg. wieku osób.

people = [('Basia', 23), ('Ania', 19), ('Katarzyna', 27), ('Ola', False, 30)]
#
# for age in people:
#     print(age[-1])



print(sorted(people, key=lambda x: x[-1]))

print(sorted(people, key=lambda x: x[-1])[::-1])
print(sorted(people, key=lambda x: x[-1], reverse=True))



import string

print(string.ascii_letters)
print(string.digits)
print(string.punctuation)
print(string.ascii_lowercase)
print(string.ascii_uppercase)

# dany jest moduł string
# zbuduj funkcję do generowania haseł
# funckja powinna przyjmować następujące argumenty
# - zadana długośc hasła,
# - czy zawrzec znaki specjalne jesli True to zawrzy jeśli False to nei zawieraj
# - na koncu wymieszaj litery
