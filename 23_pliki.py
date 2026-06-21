####### PLIKI i przechowywanie danych
#
# Cykl życia zmiennych w Pythonie kończy się w momencie, kiedy program kończy się wykonywać,
# ZMIENNA jest usuwana z pamięci (pamięć RAM jest czyszczona).
# Dlatego będziemy potrzebowali zewnętrznych pomocy, które będą przechowywały dane.
# PLIKI to takie obiekty, w którym będziemy ZAPISYWAĆ, ZACZYTYWAĆ dane i używać ich później.
# Dane będziemy mogli zaczytywać nie tylko z PLIKÓW, ale też z BAZ DANYCH czy API.
#
### ZACZYTYWANIE DANYCH
# open(filepath, mode, encoding) -> FUNKCJA "open" służy do zapisu / odczytu pliku
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

# Aby zwrócić PEŁNĄ ŚCIEŻKĘ PLIKÓW, znajdujących się w katalogu postępujemy jak niżej.

### ETAP 1 – Jak to działą?

import os

katalog = 'data' # Zwróci ŚCIEŻKĘ do katalogu, w którym znajdują się interesujące nas pliki.
sciezka_katalogu = os.listdir(katalog) # Zwróci NAZWY plików znajdujących się w katalogu "data".
# My natomiast chcemy otrzymać LISTĘ ŚCIEŻEK plików, a nie jedynie LISTĘ NAZW plików.
# Następnie chcemy ZWRÓCIĆ (ZACZYTAĆ) ZAWARTOŚĆ każdego z plików.
sciezka_plikow = [f'{katalog}/{nazwa_pliku}' for nazwa_pliku in sciezka_katalogu] # Zapis w formie List Comprehension,
# gdzie "nazwa_pliku", to nazwy każdego pliku.
# Przed każdą nazwy pliku (nazwa_pliku) chcę dodać ścieżkę do katalogu (katalog), a pomiędzy nimi dodać "/".
# print(file_paths) # Wyświetli: ['data/jakis_plik.txt', 'data/losowe.txt', 'data/losowe_120.txt', 'data/plik_z_pythona.txt']
zawartosc_plikow = []

for sciezka_pliku in sciezka_plikow: # Iterujemy kolekcję ścieżek (nazw)
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
