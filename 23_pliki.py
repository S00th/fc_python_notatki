####### PLIKI i przechowywanie danych
#
# Cykl życia zmiennych w Pythonie kończy się w momencie, kiedy program kończy się wykonywać,
# ZMIENNA jest wtedy usuwana z pamięci (pamięć RAM jest czyszczona).
# Dlatego będziemy potrzebowali zewnętrznych pomocy, które będą przechowywały dane.
# PLIKI to takie obiekty, w którym będziemy ZAPISYWAĆ, ZACZYTYWAĆ dane i używać ich później.
# Dane będziemy mogli zaczytywać nie tylko z PLIKÓW, ale też z BAZ DANYCH czy API.

### ZACZYTYWANIE DANYCH
# open(filepath, mode, encoding) -> FUNKCJA "open" służy do ZAPISU / ODCZYTU pliku
# Tryby...

# filepath – ścieżka do pliku
# mode – tryb, w jakim pracujemy na pliku (np. tylko do odczytu lub do zapisu) głównie 3, ale jest ich więcej.
# encoding – sposób kodowania znaków

# Najczęściej używane TRYBY (MODE) funkcji open()
# – 'r' (read): Tryb ODCZYTU (domyślny). Plik musi istnieć, w przeciwnym razie wystąpi błąd.
#   Używany, gdy musisz pobrać dane z pliku (np. odczytać konfigurację lub bazę danych w formacie tekstowym).
#   Domyślnym sposobem otwierania plików w Pythonie (jeśli nie określisz tryb, Python założy, że pracujesz na tekście)
#
# – 'w' (write): Tryb ZAPISU. Jeśli plik istnieje, zostanie całkowicie nadpisany. Jeśli nie istnieje, zostanie utworzony.
#   Wykorzystywany do tworzenia nowych plików wynikowych lub raportów, gdzie stara zawartość nie jest już potrzebna.
#
# – 'a' (append): Tryb DOPISANIA. Dane są dodawane na końcu pliku, nie niszcząc jego dotychczasowej zawartości.
#   Kluczowy w logowaniu zdarzeń (logach), gdzie chcesz sukcesywnie dodawać nowe informacje do istniejącego pliku bez utraty historii.
#
# – 'x' (exclusive creation): Tryb TWORZENIA pliku. Zwraca błąd, jeśli plik o danej nazwie już istnieje.



### Tryb ODCZYTU pliku – tryb 'r' (przy pomocy metody ".read")
#
file = open('data/jakis_plik.txt') # "open" zwraca obiekt, GOTOWY DO ODCZYTU ZAWARTOŚCI, ale sam nie jest zawartością.
# Ścieżka do pliku, argument domyślny (domyślnie jest to "r", więc nie trzeba go podawać)
print(file) # Wyświetli: <_io.TextIOWrapper name='data/jakis_plik.txt' mode='r' encoding='cp1250'>


### Aby ODCZYTAĆ zawartość na OBIEKCIE PLIKU, wywołujemy na nim metodę ".read", która zwraca jego zawartość.
#
content = file.read()
print (content) # Zaczyta zawartość pliku. Może tutaj wystąpić problem z ENCODINGiem (np. wyświetli: ĹĽĂłĹ‚Ä‡).
# Jeżeli spodziewasz się polskich znaków w pliku, najprawdopodobniej będziesz potrzebował encodingu utf-8.

file = open('data/jakis_plik.txt', encoding='utf-8') # Dodajemy zmienną ENCODING
content2 = file.read()
print (content2) # Wyświetli: żółć


# Raz wywołana na pliku metoda "read", "ustawi się" na ostatniej jego linii i tam zostanie.
# Jeżeli na tej samej instancji wywołam "read" ponownie, to zawartości będzie pusta,
# bo poniżej ostatniej linii już nic więcej nie ma.

file = open('data/jakis_plik.txt', encoding='utf-8')
content = file.read()
print (f'PIERWSZY kontent: \n{content}')
file.close()

file = open('data/jakis_plik.txt', encoding='utf-8')
content = file.read()
print (f'DRUGI kontent: {content}')

# Wyświetli:
#
# Pierwszy kontent:
# linia tekstu 1
# linia tekstu 2
# linia tekstu 3
# żółć # Pierwsze wywołanie metody "read" zatrzymało się na końcu tego wiersza,
# Drugi kontent: # dlatego drugi "content" jest pusty


# Poprawny PRZEPŁYW pracy z PLIKAMI wygląda w następujący sposób.
# 1. OTWARCIE pliku z użyciem FUNKCJI "open"
# 2. Wywołanie METODY ".write()" lub ".read()"
# 3. ZAMKNIĘCIE pliku metodą ".close()"

file = open('data/jakis_plik.txt', encoding='utf-8')
content = file.read()
print (f'PIERWSZY kontent: \n{content}')
file.close()

file = open('data/jakis_plik.txt', encoding='utf-8')
content = file.read()
print (f'DRUGI kontent: \n{content}')
file.close()

# Wyświetli:
#
# PIERWSZY kontent:
# linia tekstu 1
# linia tekstu 2
# linia tekstu 3
# żółć
# DRUGI kontent:
# linia tekstu 1
# linia tekstu 2
# linia tekstu 3
# żółć


####### CONTEXT MANAGER WITH – Aby plik został zamknięty, nawet jeśli wystąpi BŁĄD ########
#
# Niekiedy w trakcie pracy może wystąpić błąd.
# Żeby w momencie ewentualnego błędu zamknąć od razu plik, będziemy korzystać z CONTEXT MANAGER WITH.
# Po wyjściu z "with" plik zamknie się automatycznie. Nie trzeba pisać "close".
# Pracując z plikami, ZAWSZE korzystaj z CONTEXT MANAGER WITH.
# Będzie się on także pojawiał podczas pracy z bazą danych.

# Zamiast
file = open('data/jakis_plik.txt', encoding='utf-8')
# piszemy:
with open('data/jakis_plik.txt', encoding='utf-8') as file: # Gdzie "file" to dowolna nazwa zmiennej
    content = file.read() # Wszystko robimy w PLIKU, robimy we wcięciu
    print (content) # Nie trzeba pisać "close"



####### Tryb ZAPISU plik – tryb 'w' (przy pomocy metody ".write")
#
# Do każdej interakcji z plikiem wykorzystujemy "open". Nie tylko do otwierania.
# Jeżeli plik NIE ISTNIEJE, to zostaje UTWORZONY nowy plik.
# Jeżeli plik o podanej nazwie ISTNIEJE, to nowy plik NADPISZE stary.
# Używamy po to, aby np. zapisywać jakiś proces.

with open('data/plik_z_pythona.txt', 'w', encoding='utf-8') as file:
    file.write('To jest PIERWSZA linia nowego pliku\n') # W nawiasie wpisujemy TREŚĆ/TEKST, którą chcemy dodać do pliku.
    file.write('To jest DRUGA linia nowego pliku\n') # ZAWSZE dodajemy znacznik nowej linii na końcu każdego wiersza.



### Tryb DOPISANIA do pliku – tryb 'a' (przy pomocy metody ".append")
#
# Na końcu pliku dopisuje nowe wartości.
# Jeżeli plik NIE ISTNIEJE, to zostaje UTWORZONY nowy plik (działa jak 'w').
# Jeżeli plik o podanej nazwie ISTNIEJE, to nie nadpisuje go, tylko DOPISUJE WARTOŚCI na końcu.

with open('data/plik_z_pythona.txt', 'a', encoding='utf-8') as file:
    file.write('Jeszcze jedna linijka\n') # Dodaje jeszcze jedną linię tekstu w pliku.



### ZADANIE
#
# Wygeneruj 120 losowych liczb z danego zakresu, zapisz do pliku, tylko te liczby, które są podzielne przez 3.
# Każda linia w pliku powinna zawierać informacje o dacie i godzinie wylosowania, a także wartość tej liczby.
# Format daty: Wylosowano 2026.06.16 12:23:56 – liczba: 45

import random
from datetime import datetime
import time

with open('data/losowe.txt', 'w', encoding='utf-8') as file: # Tworzymy PLIK jeden raz, na początku pracy programu.
    for number in range(15):
        time.sleep(2) # Przy każdej iteracji Python poczeka 2 sekundę (opóźniamy iteracje)
        num = random.randint(0, 1000)
        if num % 3 == 0:
            now_str = datetime.now().strftime('%Y.%m.%d %H:%M:%S')
            file.write(f'Wylosowano: {now_str} – Liczba: {num}\n')



####### Praca na WIELU plikach
#
# Mając kolekcję ścieżek, trzeba przeiterować się przez wszystkie pliki.
# Nie ważne, na jakich plikach pracujemy (txt, csv, exel itp.).
# Możemy to zrobić na 2 sposoby. ZAPYTAĆ o DRUGI sposób !!!


# FUNKCJA: ".getcwd"
print(os.getcwd()) # Zwróci aktualną ŚCIEŻKĘ ROBOCZĄ katalogu (Get current working directory)
# Wyświetli: Y:\Py\FC\fc_python_notatki

# FUNKCJA: ".listdir"
print(os.listdir('data')) # Zwróci LISTĘ NAZW plików z katalogu. Jako argument przyjmuje NAZWĘ katalogu.
# Wyświetli: ['jakis_plik.txt', 'losowe.txt', 'losowe_120.txt', 'plik_z_pythona.txt']



####### ĆWICZENIE – Tworzenie LISTY
# LISTA zawiera elementy składające się z NAZWY PLIKÓW i ŚCIEŻKI do katalogu, w którym te pliki się znajdują.

import os

katalog = 'data'
lista_nazwy_plikow_w_katalogu = os.listdir(katalog)

### METODA 1 – Zapis w formie List Comprehension:
# WAŻNE! List Comprehension automatycznie tworzy LISTĘ
lista_sciezek_plikow_1 = [f'{katalog}/{nazwa_pliku}' for nazwa_pliku in lista_nazwy_plikow_w_katalogu]

### METODA 2 – Zapis w formie pętli "for":
# WAŻNE! W przeciwieństwie do List Comprehension pętla "for" NIE tworzy LISTY.
# Musisz zainicjalizować pustą listę, a wewnątrz pętli użyć METODY .append(), aby dodawać do niej kolejne elementy.
lista_sciezek_plikow_2 = []
for nazwa_pliku in lista_nazwy_plikow_w_katalogu:
    sciezka = f'{katalog}/{nazwa_pliku}'
    lista_sciezek_plikow_2.append(sciezka)  # KROK 2: Dokładamy element do listy

print(lista_sciezek_plikow_1)
print(lista_sciezek_plikow_2)



# Aby zwrócić PEŁNĄ ŚCIEŻKĘ PLIKÓW, znajdujących się w katalogu postępujemy jak niżej.

### ETAP 1 – Jak to działą?

import os

katalog = 'data' # Zwróci ŚCIEŻKĘ do katalogu, w którym znajdują się interesujące nas pliki.
lista_nazwy_plikow_w_katalogu = os.listdir(katalog) # Zwróci NAZWY plików znajdujących się w katalogu "data".
# My natomiast chcemy otrzymać LISTĘ ŚCIEŻEK plików, a nie jedynie LISTĘ NAZW plików.
# Następnie chcemy ZWRÓCIĆ (ZACZYTAĆ) ZAWARTOŚĆ każdego z plików.
lista_sciezek_plikow = [f'{katalog}/{nazwa_pliku}' for nazwa_pliku in lista_nazwy_plikow_w_katalogu] # Zapis w formie List Comprehension,
# DLA każdego PLIKU z LISTY PLIKÓW znajdujących się w KATALOGU:
# – Przed każdą NAZWĄ PLIKU dodaj ŚCIEŻKĘ do katalogu.
# – Pomiędzy ŚCIEŻKĄ KATALOGU, a NAZWA PLIKU dodaj "/".
# print(file_paths) # Wyświetli: ['data/jakis_plik.txt', 'data/losowe.txt', 'data/losowe_120.txt', 'data/plik_z_pythona.txt']
zawartosc_plikow = []

for sciezka_pliku in lista_sciezek_plikow: # Iterujemy kolekcję ścieżek (nazw)
    with open(sciezka_pliku, encoding='utf-8') as f: # Otwieram każdy plik i dla każdego dodaję "file_paths"
        zawartosc = f.read() # Zaczytuje plik po pliku, a "zawartosc" dodaję do listy pustej "zawartosc_plikow"
        zawartosc_plikow.append(zawartosc) # ŁĄCZYMY i ZAPISUJEMY zawartość do jednego pliku.

print(zawartosc_plikow)
# print(zawartosc_plikow[0]) # Wyświetli zawartość tylko pierwszego pliku z listy (pierwszego w katalogu).


### ETAP 2 – Działający kod

root = 'data'
data_dir = os.listdir(root)
file_paths = [f'{root}/{filename}' for filename in data_dir]
files_content = []

for file_path in file_paths:
    with open(file_path, encoding='utf-8') as f:
        content = f.read()
        files_content.append(content)

print(files_content)



###### ZADANIE DOMOWE
#
# Zaczytaj pliki z folderu "Data2" na takiej zasadzie, żeby otrzymać mapping,
# gdzie kluczem będzie NAZWA pliku, a WARTOŚCIĄ, zawartość tego pliku (nie wrzucamy do LISTY).

import os

katalog = "data"
lista_nazwy_plikow_w_katalogu = os.listdir(katalog) # Lista nazw plików
lista_sciezek_plikow = [f"{katalog}/{nazwa_pliku}" for nazwa_pliku in lista_nazwy_plikow_w_katalogu] # Lista ścieżek
moj_slownik = {}

for index in range(len(lista_nazwy_plikow_w_katalogu)): # Iteruj się po wszystkich plikach (indeksach) w katalogu (w LIŚCIE)
    # len sprawdza, ile plików jest w katalogu, a pętla "for" działa tyle razy, ile jest plików w katalogu.
    sciezka = lista_sciezek_plikow[index] # Zwróć ŚCIEŻKĘ pliku
    nazwa = lista_nazwy_plikow_w_katalogu[index] # Zwróć NAZWĘ pliku
    with open(sciezka, encoding="utf-8") as plik: # Otwórz i zazzytaj zawartość plików
        moj_slownik[nazwa] = plik.read()

print(moj_slownik)



####### Praca z plikami CSV
#
# Plik tekstowy jest przykładem danych nieustrukturyzowanych (plik zawiera: imiona, nazwiska, wiek w różnej kolejności)
# W Pythonie (w analizie danych) często będziemy spotykali pliki, które będa USTRUKTURYZOWANE (też obraz albo video)
# Dane USTRUKTURYZOWANE (w ujęciu analizy danych) to dane zapisane w FORMIE TABELARYCZNEJ.
# Zawartość takiego pliku może wyglądać jak niżej.
#
# Imię;nazwisko;wiek # Header
# Ewa;Kowalczyk;40 # Wiersze i kolumny. Inaczej zapisana tabela z exela.
# Jan;Mazur;50
#
# Ważne! Wyświetlając w PyCharm plik CSV możemy przełączyć widok (na dole okna) na "Data" (tabelkę) lub "Text".

# Przykładem plików ustrukturyzowanych są pliki CSV (Coma Separated Values).
# Oczywiście wbrew na nazwie mamy dostępne także inne separatory (np. jak w przykładzie średnik).
# W Pythonie do obsługi plików CSV służy moduł CSV (jest częścią biblioteki standardowej).


import csv

# ZACZYTANIE / OTWIERANIE plik
with open("data/csv_files/csv.csv", encoding="utf-8") as file:
    content = file.read()

print(content)



# Otwieranie pliku CSV jako LISTY LIST, gdzie każdy wiersz (OSOBA) jest osobną LISTĄ.

with open("data/data.csv", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=";") # Użyj modułu csv. Jako argument przyjmie "file", gdzie separatorem jest ;

    for row in reader:
        print(row) # Zaczytanie CSV jako LISTY

print(reader) # import csv

# ZACZYTANIE / OTWIERANIE plik
with open("data/csv_files/csv.csv", encoding="utf-8") as file:
    content = file.read()

print(content)



# Otwieranie pliku CSV jako LISTY LIST, gdzie każdy wiersz (OSOBA) jest osobną LISTĄ.

with open('data/data.csv', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=';') # Użyj modułu csv. Jako argument przyjmie "file", gdzie separatorem jest ;

    for row in reader:
        print(row) # Zaczytanie CSV jako LISTY

print(reader) # import csv

# ZACZYTANIE / OTWIERANIE plik
with open("data/csv_files/csv.csv", encoding="utf-8") as file:
    content = file.read()

print(content)



# OTWIERANIE pliku CSV jako oddzielonej średnikami LISTY, gdzie każdy wiersz (OSOBA) jest osobną LISTĄ.

with open("data/csv_files/csv.csv", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=";") # Jest to iterator. Użyj modułu csv.
    # Jako argument przyjmie "file", gdzie separatorem jest ";" (czyli separator użyty w pliku csv).

    for row in reader: # Przeiteruj się po iteratorze.
        print(row) # Zaczytanie CSV jako LISTY, każdy to listą. Wyświetli: ['imie', 'nazwisko', 'wiek']

print(reader) # Wyświetli: <_csv.reader object at 0x00000205D0A84F40>. Jest to jakiś plik w pamięci.



# ZACZYTANIE pliku CSV jako oddzielonego średnikami SŁOWNIKA (gdzie każdy wiersz jest osobnym słownikiem)

with open("data/csv_files/csv.csv", encoding="utf-8") as file:
    reader = csv.DictReader(file, delimiter=';') # Gdzie separatorem jest ";" (separator użyty w pliku csv).
    # print(list(reader))
    for row in reader: # Iterujemy się po SŁOWNIKACH, gdzie każdy wiersz to SŁOWNIK
        print(row) # Wyświetli: {"imie": "Jan", "nazwisko": "Mazur", "wiek": "50"}
        print(row["imie"], row["nazwisko"], row["wiek"]) # Z każdego słownika wyciągamy wartości po kluczu: Jan Mazur 50
                                                         # Nazwa klucza to HEADER (imie;nazwisko;wiek)

    print(list(reader)) # Reader to iterator więc możemy go zamienić na listę, ale po przeiterowaniu się jest on pusty.
                        # Dlatego trzeba go wyświetlić zaraz po wywołaniu (wiersz 351)



####### TWORZENIE pliku CSV
# CSV writer

import csv

# Mamy następujące dane (LISTA LIST) i chcemy je zapisać do pliku
dane = [
    ["imie", "nazwisko"], # Nagłówek
    ["Anna", "Nowak"], # Wiersze
    ["Piotr", "Kowalski"]
]


### METODA "writerow" (wpisz pojedynczy wiersz)
# Musimy mieć przygotowane wcześniej dane w jakiejś strukturze (jak wyżej), przeiterować się po nich i każdy element zapisać.

with open("data/csv_files/csv3.csv", mode="w", encoding="utf-8", newline="") as file:
    # Argument "newline" ustawiamy na pusty string, aby nowa linia była pusta, a nowa zawartość wpisana od nowej linii.
    # Nie trzeba go stosować w plikach tekstowych (bo używamy w nich \n),
    # natomiast w plikach csv, mamy nowy wiersz dodawany przy każdej iteracji.
    writer = csv.writer(file) # Instancja writera, który przyjmie jako argument "file"

    for row in dane: # Iterujemy się po danych
        writer.writerow(row) # Wpisz pojedynczy wiersz

# W plikach csv zaznaczamy znak nowej linii, używając argumentu "newline" (w plikach tekstowych \n).


### METODA "writerows" (zapisz wszystkie wiersze).
# Bez potrzeby użycia pętli.

with open("data/csv_files/csv3.csv", mode="w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(dane)

# WAŻNE! Trzeba znać obie metody.
# Było to pisanie LISTY LIST.



# Co zrobić, kiedy mamy mieli do czynienia z danymi przygotowanymi w inny sposób?
##### LISTA SŁOWNIKÓW

dane2 = [
    {"imie": "Anna", "nazwisko": "Nowak"},
    {"imie": "Piotr", "nazwisko": "Kowalski"}
]

# Kształt danych, jakie mamy na dzień dobry, będzie determinował czy skorzystamy z "writer", czy "DictWriter".

### METODA "DictWriter"
# Będzie idealna, gdy dane wejściowe są SŁOWNIKAMI (np. z API lub baz danych).
# Gdzie nazwy pól, to KLUCZE ze SŁOWNIKA.

### Metoda "writerows"
# Będzie idealna, gdy dane wejściowe są LISTAMI 2D.
# Gdzie każdy wiersz, to osobna lista, a pierwsza LISTA to HEADER.

with open("data/csv_files/csv4.csv", mode="w", encoding="utf-8", newline='') as file:
    fieldnames = {"imie", "nazwisko"} # Wymagany jest parametr nazwy pól, którymi będą klucze ze słownika
    writer = csv.DictWriter(file, fieldnames=fieldnames) # Tworzymy instancję "writera" robimy z "DictWriter"
                                                         # Jednak NAGŁÓWEK nie zostanie zapisany.
    writer.writeheader() # Dlatego, kiedy pracujemy na SŁOWNIKACH najpierw tworzymy HEADER
    writer.writerows(dane2) #  i dopiero teraz możemy wpisać dane.



### PRZYKŁAD
#
# Filtrowanie osób powyżej 18 roku życia
# 1. Zaczytaj dane z pliku osoby.csv
# 2. Zapisz do pliku pełnoletni.csv tylko te wpisy, gdzie osoba ma powyżej 18 lat.
# 3.

import csv

# Zaczytanie do pliku osoby.csv
with open("data/csv_files/osoby.csv", encoding="utf-8") as plik_wejsciowy:
    reader = csv.DictReader(plik_wejsciowy)
    # print(list(reader)) # Wyświetlamy LISTĘ

    pelnoletni = [] # Utwórz pustą LISTĘ
    for osoba in reader: # Zmienna osoba jest SŁOWNIKIEM
        if int(osoba["wiek"]) >= 18: # Iteruj się po KLUCZU "wiek" w każdym SŁOWNIKU (osoba) i jeśli...
            print(osoba) # Powstaje LISTA.
            pelnoletni.append(osoba) # Dodajemy do LISTY.
        print(pelnoletni)

# print(osoba["osoba"]) # Metoda getitem. Gdy nie ma klucza, podnosi błąd.
# print(osoba.get["wiek"]) # Metoda get. Gdy nie ma klucza, nie podnosi błędu i zwraca "None".

# Zapisywanie do pliku pełnoletni.csv
with open("data/csv_files/pełnoletni.csv", mode="w", encoding="utf-8", newline="") as plik_wyjsciowy:
    writer = csv.DictWriter(plik_wyjsciowy, fieldnames=["imie", "nazwisko", "wiek"])
    writer.writeheader()
    writer.writerows(pelnoletni)


# Zapis w jednej linii

    with open("data/csv_files/osoby.csv", encoding="utf-8") as plik_wejsciowy:
        reader = csv.DictReader(plik_wejsciowy)

        pelnoletni = [osoba for osoba in reader if int(osoba["wiek"]) >= 18] # List comprehension automatycznie tworzy listę.

    with open("data/csv_files/pełnoletni.csv", mode="w", encoding="utf-8", newline="") as plik_wyjsciowy:
        writer = csv.DictWriter(plik_wyjsciowy, fieldnames=["imie", "nazwisko", "wiek"])
        writer.writeheader()
        writer.writerows(pelnoletni)



# Plik CVS jest plikiem PŁASKIM
#

data1 = ['Danusia', 'Kowalska', 35, 'HR']
data2 = ['Grzegorz', 'Nowak', 23, 'IT'] # Lista list jest zbiorem danych płaskich (prostych, niezagnieżdżonych).

# Jeżeli do tego typu informacji chciałbym dodać więcej informacji, np.
# adres: ulica, nr budynku, kod pocztowy, miasto
# zainteresowania: nazwa, ile h tygodniowo, z kim (imiona osób, z którymi spędza czas przy hobby)
# partner: imię partnera, wiek partnera, płeć, czy ma samochód
#
# W tym momencie odchodzimy od jednowymiarowości danych
# Będziemy potrzebowali zgnieżdzonej struyktóry danych
# Chceby przekształcić tego typu dane w słownik

data3 = {
    'imie': 'Danusia',
    'nazwisko': 'Kowalska',
    'wiek': 35,
    'zawod': 'HR'
    'adres': {
        'ulica': 'Czekoladowa',
        'nr_budynku': '12a',
        'miasto': 'Wrosław'
    },
    'hobby': {
        'nazwa': 'siatkówka',
        'ile_h_per_tydzien': 5
    },
    'partner': {
        'Imie': 'tomek',
        'wiek': 40
        'Plec': 'M',
        'wiek': 40
    }
    'partner': None
}

# Json (JavaScript Obiect Notation) – Jakby słownik, ale zapisany w formie tekstu.
# Systemy przesyłają pomiędzy sobą i muszą w taki sam ujmować dane
#

import json

# Moduł wbudownay

with open('json_files/person1.json', 'w', encoding='utf-8') as f:
    json = json.dumps(person1, f, ensure_ascii=False, indent=4) # Indent dodaje informację o wcięciu wielkosci 4 spacji
# ensure_asci=False # Aby obsługiwane były polskie znaki (warto dodać dla PyCharma, w VSC nie ma problemu)
# W Pythonie typuy danych BOOL (False, Frue) pisze sie w duzej litery a w innych technologiach z małej
# typ danych json jest swego rodzaju językiem angielskim w komunikacji między systemami
#
# SERILIZACJA – to PROCES konwersji z typu natywnego (np. obiekt python) na json
# DeSERILIZACJA – to PROCES konwersji z json na typ natywny (np. obiekt python)
# Funkcja "json.dump" SERIALIZUJE obiekt pythonowy i zapisuje do pliku (i przerabia na słownik)
# Funkcja "json.load" ZACZYTUJE dane z pliku i DeSERIALIZUJE je na obiekt pythonowy (i zapisuje do pliku)

with open('json_files/person1', encoding='utf-8') as f:
    loaded_person1 = json.load(f)

print(loaded_person1) # Wyświetli w jednym wierszu


from pprint import pprint #

with open('json_files/person1', encoding='utf-8') as f:
    loaded_person1 = json.load(f)



# WIELE obiektów

persons = [person1, person2]

with open('json_files/persons.json', 'w', encoding='utf-8') as f:
    json = json.dumps(persons, f, ensure_ascii=False, indent=4)

# Pojedynczy słownik to OBIEKT
# Lista słowników to TABLICA (kolekcja obiektów)

with open('json_files/persons', encoding='utf-8') as f:
    loaded_persons = json.load(f)

print(type(loaded_persons)) # Wyświetli <class 'list'>
print(len(loaded_persons))
pprint(loaded_persons[0])
pprint(loaded_persons[1])
pprint(loaded_persons[0]['hobby']['zespol'][0])



### ZADANIE – JSON bez DeSERIALIZACJI
#

with open('json_files/persons', encoding='utf-8') as f:
    data = f.read()

print(type(data))

# Jeśli dostaniemy dane np. z sieci, trzeba będzie z nimi coś zrobić (deserialisować)
# Z uwagi na to, że "data" to czysty json, czyli technicznie rzeczy biorąc napis, muszę go zdeserializować,
# żeby zamienić na typ danych pyhonowy, aby móc na nim pracować.

deserialized_data = json.loads(data) # DESERIALISUJE "data"
print(type(deserialized_data))
print(deserialized_data[0]['nazwisko'])

# funkcja "load" to 2 funkcjonalności: odczyt jsona z pliku i deserializacja
# funkcja "loads" to 1 funkcjonalność: tylko deserializacja strungu czystego jsona

json_data = '''
    {
    uzupełnić
    }
'''

print(type(json_data))
from_json = json.loads(json_data)
print(type(from_json))

# Nie ważne, że będziemy mieli to w kodzie czy w pliku, deserializacja odbędzie się...


# json MUSI posiadać poprawne FORMATOWANIE
# Jets podobry do słownika pyhonowego, ale nie zawsze tak będzie.
# Jednak json nie wszystko przyjmie.
# np. po ostatnie parze klucz-wartość nie może być przecinka (wyświetli błąd)
# klucz czy wartość w apostrofach też jest niedozwolona.
# Dlatego istnieje coś takeigo jak https://jsonlint.com/ (jets to formater / validator)
# Dodajemy tu coś, co chcemy zdeserializować i sprawdzamy (validate)



# Mam słownik, który chcę zserializować, ale nie zapisywać do pliku (czysta serializacja)
#

json_data = json.dumps(person1, ensure_asci=False)
print(json_data)
print(type(json_data))

# funkcja "dump" to 2 funkcjonalności: serializacja i zapis jsona do pliku
# funkcja "dumps" to 1 funkcjonalność: tylko deserializacja obieku pythonowego na json

