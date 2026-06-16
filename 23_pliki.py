####### PLIKI i przechowywanie danych
#
# Cykl życia zmiennych w Pythonie kończy się w momencie, w którym program się kończy – pamięć (RAM) jest czyszczona.
# Dlatego będziemy potrzebowali zewnętrznych pomocy, które będą przechowywały dane.
# PLIKI to taki obiekt, w którym będziemy mogli zapisywać i zaczytywać dane.
# Dane będziemy mogli zaczytywać z PLIKÓW, z baz danych czy API.
#
### ZACZYTYWANIE DANYCH
# open(filepath, mode, encoding) -> FUNKCJA "open" służy do zapisu / odczytu pliku
# Tryby...


# ODCZYT pliku
file = open('data/jakis_plik.txt', ) # open zwraca obiekt, gotowy do odczytu zawartości. Sam nie jest zawartością.
# Ścieżka do pliku, argument domyślny (domyślnie jest to "r")

print(file) # Wyświetli: <_io.TextIOWrapper name='data/jakis_plik.txt' mode='r' encoding='cp1250'>

# Aby odczytać zawartość, na OBIEKCIE PLIKU wywołujemy metodę .read, która zwraca jego zawartość.
content = file.read()
print (content) # Zaczyta zawartość pliku. Może tutaj wystąpić problem z ENCODINGiem (wyświetli: ĹĽĂłĹ‚Ä‡).

file = open('data/jakis_plik.txt', encoding='utf-8')
content2 = file.read()
print (content2) # Wyświetli: żółć

print (f'Drugi content: {content2}')

# Jeśli raz wywołamy metodę "read" na pliku, to "ustawiamy sięna ostatniej jego linii i tam zostajemy,
# zatem jeśli na tej samej instancji wywołam "read" ponownie do zawartości będzie pusta,
# bo poniżej ostatniej linii już nic więcej nie ma.

# Poprawny PRZEPŁYW pracy z PLIKAMI.
# 1. Otwarcie pliku z użyciem FUINKCJI "open"
# 2. Wywołanie metody "write" lub "read"
# 3. Zamknięcie pliku

file = open('data/jakis_plik.txt', encoding='utf-8')
content = file.read()
print (f'Pierwszy content: {content}')
file.close()

file = open('data/jakis_plik.txt', encoding='utf-8')
content = file.read()
print (f'Drugi content: {content}')
file.close()


### Context menager with
#
# Niekiedy w trakcie pracy może wystąpić błąd.\
# Żeby w momencie ewentualnego błędu zamknąć od razu plik, będziemy korzystać z "context menagera with".
# Nie trzeba pisać "close", po wyjściu z "with" plik zamknie się automatycznie.
# Pracując z plikami, ZAWSZE korzystamy z "context menager with".

with open('data/jakis_plik.txt', encoding='utf-8') as file: # Gdzie "file" to dowolny wyraz
    content = file.read()
    print (content)


### ZAPIS plików – mode w (przy pomocy metody "write")
#
# Do każdej interakcji z plikiem wykorzystujemy "open". Nie tylko do otwierania.
# Jeśli plik nie istnieje, to zostaje UTWORZONY, a jeśli istnieje, to nowy plik NADPISUJE stary.
# Pliki używamy po to, aby np. zapisywać jakiś proces

with open('data/plik_z_pythona.txt', 'w', encoding='utf-8') as file:
    file.write('To jest PIERWSZA linia nowego pliku\n') # ZAWSZE dodajemy znacznik nowej linii na końcu każdego wiersza.
    file.write('To jest DRUGA linia nowego pliku\n')


### ZADANIE
#
# Wygeneruj 120 losowych liczb z danego zakresu, zapisz do pliku, tylko te liczby, które są podzielne przez 3.
# Każda linia w pliku powinna zawierać informacje o dacie i godzinie wylosowania, a także wartość tej liczby.
# Format daty: 2026-06-16 12:23:56 – liczba: 45

import random
from datetime import datetime, time

with open('data/losowe_120.txt', 'w', encoding='utf-8') as file: # Tworzymy PLIK jeden raz, na początku pracy programu.
    for number in range(120):
        # time.sleep(1) # Przy każdej iteracji Python poczeka 1 sekundę
        num = random.randint(0, 10_000)
        if num % 3 == 0:
            now_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            file.write(f'{now_str} – liczba: {num}\n')


### Tryb a – append
#
# Na końcu pliku dopisuje nowe wartości.
# Jeśli plik nie istnieje, to go tworzy (działa jak "w").
# Jeśli plik nie istnieje, to nie nadpisuje go, tylko dopisuje wartości na końcu.

with open('data/plik_z_pythona.txt', 'a', encoding='utf-8') as file:
    file.write('Jeszcze jedna linijka\n') # Dodaje jeszcze jedną linię tekstu w pliku.


# Praca na WIELU plikach
#
# Mając kolekcję ścieżek, trzeba będzie przeiterować się przez wszystkie pliki.
# Nie ważne, na jakich plikach pracujemy (txt, csv, exel itp.)
# Możemy to zrobić na 2 sposoby.

import os

root = 'data2'
data_dir = os.listdir(root)
file_paths = [f'{root}/{filename}' for filename in data_dir] # Gdzie filename to nazwa każdego pliku

files_content = []
for file_path in file_paths:
    with open(file_path, encoding='utf-8') as f:
        content = f.read()
        files_content.append(content)

print(files_content)



###### ZADANIE DOMOWE
#
# Zaczytaj pliki z folderu "Data2" na takiej zasadzie, żeby otrzymać mapping,
# gdzie kluczem będzie NAZWA pliku, a WARTOŚCIĄ, zawartość tego pliku.
