
###### ZADANIE DOMOWE
#
# Zaczytaj pliki z folderu "Data2" na takiej zasadzie, żeby otrzymać mapping,
# gdzie kluczem będzie NAZWA pliku, a WARTOŚCIĄ, zawartość tego pliku (nie wrzucamy do LISTY).


# import os
#
# katalog = 'data'
# sciezka_katalogu = os.listdir(katalog) # Zwróci NAZWY plików znajdujących się w katalogu "data".
# # My natomiast chcemy otrzymać LISTĘ ŚCIEŻEK plików, a nie jedynie LISTĘ NAZW plików.
# # Następnie chcemy ZWRÓCIĆ (ZACZYTAĆ) ZAWARTOŚĆ każdego z plików.
# sciezka_plikow = [f'{katalog}/{nazwa_pliku}' for nazwa_pliku in sciezka_katalogu] # Zapis w formie List Comprehension,
# # DLA każdego PLIKU w KATALOGU:
# # – Przed każdą nazwy pliku (nazwa_pliku) chcę dodać ścieżkę do katalogu (katalog)
# # – Pomiędzy ŚCIEŻKĄ KATALOGU, a NAZWA PLIKU dodaj "/".
# print(file_paths) # Wyświetli: ['data/jakis_plik.txt', 'data/losowe.txt', 'data/losowe_120.txt', 'data/plik_z_pythona.txt']
# zawartosc_plikow = {}
#
# for sciezka_pliku in sciezka_plikow: # Iterujemy kolekcję ścieżek (nazw)
#     with open(sciezka_pliku, encoding='utf-8') as f: # Otwieram każdy plik i dla każdego dodaję "file_paths"
#         zawartosc = f.read() # Zaczytuje plik po pliku, a "zawartosc" dodaję do listy pustej "zawartosc_plikow"
#         zawartosc_plikow.append(zawartosc) # ŁĄCZYMY i ZAPISUJEMY zawartość do jednego pliku.
#
# print(zawartosc_plikow)



# for i in range(0, 20):
#     if i % 3 == 0:
#         numbers.append(i)
# my_range = [i for i in range(0, 20) if i % 3 == 0]
#
# [f'{katalog}/{nazwa_pliku}' for nazwa_pliku in sciezka_katalogu]
#
# for nazwa_pliku in sciezka_katalogu:
#     f'{katalog}/{nazwa_pliku}'

# sciezka_plikow = [f'{katalog}/{nazwa_pliku}' for nazwa_pliku in sciezka_katalogu]
# print(sciezka_plikow)



# for key, val in dict.items():
#     print(f'KEY: {key} VA: {val}')
#
# dict['waga'] = 55 # <nazwa słownika>['KLUCZ'] = WARTOŚĆ



import os

katalog = 'data'
lista_nazwy_plikow_w_katalogu = os.listdir(katalog) # Lista nazw plików
lista_sciezek_plikow = [f'{katalog}/{nazwa_pliku}' for nazwa_pliku in lista_nazwy_plikow_w_katalogu] # Lista ścieżek
moj_slownik = {}

for index in range(len(lista_nazwy_plikow_w_katalogu)): # Iteruj się po wszystkich plikach (indeksach) w katalogu (w LIŚCIE)
    # len sprawdza, ile plików jest w katalogu, a pętla "for" działa tyle razy, ile jest plików w katalogu.
    sciezka = lista_sciezek_plikow[index] # Zwróć ŚCIEŻKĘ pliku
    nazwa = lista_nazwy_plikow_w_katalogu[index] # Zwróć NAZWĘ pliku
    with open(sciezka, encoding='utf-8') as plik: # Otwórz i zazzytaj zawartość plików
        moj_slownik[nazwa] = plik.read()

print(moj_slownik)
