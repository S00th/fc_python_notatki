name = 'Darek'
last_name = 'Nowak'

# konkatencja strigów

# 1 sposób - +
full_text = "Witam, mam na imię " + name +  " " + last_name

print(full_text)

name = 'Darek'
age = 36
height = 175.092384023984

full_text = "Witam, mam na imię " + name +  " mam " + str(age) + " lat i " + str(height) + "cm wzrostu"
print(full_text)

print(1 + 1) # dla numerycznych + zadziała jak dodawania
print('1' + '1') # dla strigów zadziała jak konkatenacja - sklejenie napisów
# print(1 + '1') # pomiedzy numerycznym a stringiem - nie zadziała

# 2 sposób - f- string
full_text = f'Witam. mam na imię {name} i mam {age} lat oraz {height:.1f} cm wzrostu'

print(full_text)






#### indeksowanie i slicing stringów  ==========================================
print("========================================== indeksowanie i slicing stringów  ==========================================")
jakis_napis = 'abcdefghijksdkjhfkdjshfkjdhsfkjdhfsddd12214'

# T E K S T
# 0 1 2 3 4 L --> P
#-5 -4 -3 -2 -1  P --> L

# syntax
# iterable[index]
# jeśli wskazany indeks nie istnieje to zostanie podniesiony błąd IndexError
# jakis_napis[10_000]

print(f"pierwsza litera napisu {jakis_napis} to {jakis_napis[0]}") # indeks 0 zawsze pierwszy element
print(f"druga litera napisu {jakis_napis} to {jakis_napis[1]}")
print(f"OSTATNIA litera napisu {jakis_napis} to {jakis_napis[-1]}") # indeks -1 zawsze ostatni element

jakis_inny_napis = 'język python mozna wykorzystać do modelowania sieci neuronowych'

# slicing - wycinanie kawałka
# syntax
# iterable[start_index: stop_index: step]
# start_index - included - domyślnie 0
# stop_index - exluded - domyślnie ostatni
# step - domyślnie 1 (ujemny step będzie oznaczać odwrócona kolejność)

print(jakis_inny_napis[0:5]) # z napisu biorę litery od indeksu 0 do indeksu 5, ale bez 5, krok
print(jakis_inny_napis[:5]) # to jest to samo co powyżej, bo start_indeks domyślnie 0 (od pcozątku do 5 ale bez 5)

print(jakis_inny_napis[14:30:2]) # wez litery od indeksu 14 do 30, bez 30, co druga literę

print(jakis_inny_napis[-11:]) # bierzemy wszystki litery od 11 od końca do końca

print(jakis_inny_napis[-11::2]) # bierzemy wszystki litery od 11 od końca do końca, co druga litera

print(jakis_inny_napis[::-1]) # cały tekst od tyłu

# nieistniejący lub cześciowo nieistniejący zakres - nie dostaniemy błędu !!!
print(jakis_inny_napis[30: 100]) # wypisze tyle ile jest
print(jakis_inny_napis[1_000: 10_000]) # nic nie wypisze bo przedział całkiem poza zakresem


# długość każdego obiektu iterowalnego można zmierzyć przy pomocy funkji wbudowanej len
print(f"długośc napisu {jakis_inny_napis} to {len(jakis_inny_napis)}")


# dany jest napis
napis = "Danusia jest fryzjerką i chodzi do technikum."
# na podatawie tego napisu podziel go na 2 rowne cześci - tj od początku do połwy i od połowy do końca
# przypisz do odpowiednich zmiennych

napis_lenght = len(napis)
print(napis_lenght)
napis_lenght_halved = napis_lenght // 2 # znalezienie indeksu środkowego
print(f"To jest połowa zadania: {napis[:napis_lenght_halved]}")
print(f"To jest druga połowa zadania: {napis[napis_lenght_halved:]}")


#### metody stringów ==========================================
print("========================================== METODY STRINGÓW ==========================================")
day = 'PONIEDZiałek'
day_sentence = 'dzisiaj jest wtorek'

print(day.upper()) # zwraca napis WIELKIMI literami
print(day.lower()) # zwraca napis małymi literam
print(day.title()) # # pierwsza litera każdego słowa w tekscie jest wielka
print(day_sentence.title())
print(day_sentence.capitalize()) # tylko pierwsza litera jest wielka

sentence = ' uczymy się pythona       '
clean_sentence = sentence.strip() # usunięcie białych znaków z początku tekstu i z końca !!!!!!!!!!!!!!!!!!

# lstrip - usunięcie z poczatku, rstrip - usunięcie z końca napisu

print(len(sentence))
print(len(clean_sentence))

# replace(old, new) - zmienia fragment tekstu na inny !!!!!!!!!!!!!!!!!!!!!
word = 'python'

# chcemy zamienić literę p na c - jest case sensitive - wazna jest wielkośc znaków
new_word = word.replace('p', 'c')
print(new_word)

# metoda replace służy także do usuwania znaków
print(word.replace('p', '')) # usunięcie litery p z tekstu --> p zamieniam na nic

# z napisu
name = 'Bartek'
# usun literę b a następnie zamień wszystkie litery na wielkie

# methods chaining
final_name_chaining = name.lower()\
    .replace('b', '')\
    .upper()

print(final_name_chaining)

# bez methods chaining - tutaj pośrednio zapisujemy wyniki
# musimy przechowac wynik danego kroku zeby móc go wykorzystac w kolejnym
name_lower = name.lower()
name_lower_remove_b = name_lower.replace('b', '')
final_name = name_lower_remove_b.upper()

print(final_name)


# metoda split(sep) !!!!!!!!!!!!!!!!!!!!!!!!
# jeśli mamy ustrukturyzowany tekst,
# gdzie każdy z elementów jest oddzielony od siebie tym samym separatorem
# to możemy wyciągnać każdy z elementów osobno
# zwraca listę stringów

names = 'basia, danusia, asia, bartek, ania'
print(names.split(', ')) # separatorem jest przecinek i spacja

languages = 'python|java|csharp|js'
print(languages.split('|'))

import os

# wypusujemy ścieżke robocza gdzie aktualnie pracujemy
print(os.getcwd()) # zwraca string ze śceiżka

# wyodrębnij każdy element scieżki jako osobny element listy
print(os.getcwd().split("\\"))

# # \ sluzy do tworzenia znakow specjalnych
# print('linia 1 \n linia 2') # znak nowej linii
# print('linia 1 \t linia 2') # znak tabulacji

# join - złącznie kolekcji - typu lista w pojedynczy string !!!!!!!!!!!!!!!!!!!!!!!
# zwraca string
lang_list = ['python', 'java', 'csharp', 'js']
# chcemy listę osobnych stringów wrzucić w jeden string

joined_string = ', '.join(lang_list)
print(joined_string)


# find - zwraca indeks znaku
# zwraca integer
# jeśli nie istnieje w tekscie to zwraca -1

word = 'python'
print(word.find('p')) # istenieje
print(word.find('w')) # nie istenieje

sentence = "python jest super"
print(sentence.find('p')) # zwraca zatem tylko pierwsze wystąpienie

print(sentence.find('per')) # mozna tez wskazać cały kawałek tekstu
print(sentence.find('hon'))

# index - działa jak find tylko gdy nie znjadzie do podnosi błąd
# word = 'python'
# print(word.index('w'))

# count - zwraca liczbę wystapień
# zwraca integer
sentence = "python jest super"
print(sentence.count('p')) # ile liter p występuje w tekscie
print(sentence.count('x'))

# startswith - sprawdza czy dany napis zaczyna się od danego prefiksu !!!!!!!!!!!!!!!!!!!!!!!!!!!!
# zwraca bool

word = 'python'

print(word.startswith('p')) # czy wyraz python zaczyna się na p
print(word.startswith('x')) # czy wyraz python zaczyna się na x

print(word.startswith('pic')) # czy wyraz python zaczyna się na pic
print(word.startswith('pyt')) # czy wyraz python zaczyna się na pyt


# endswith - sprawdza czy dany napis kończy się danym suffixem
# zwraca bool

filename = 'data.csv'
print(filename.endswith('.csv')) # czy rozszerzenie pliku to .csv (czy nazwa pliku koczy się na wyraz csv)


# dana jest nazwa pliku
filename = 'tabela.xlsx'

# filename = 'xlsxtabela.parquet'
# bez uzycia metody endswith sprawdz czy jest rozszerzenia .xlsx
print(filename[-5:] == '.xlsx')

# isaplha - sprawdza czy wszystkie znaki to litery alfabetu
# zwraca bool

word = 'python'
print(word.isalpha())

word = 'python123'
print(word.isalpha()) # false bo string zawiera napisy ktre nie ca literami

word = 'python@.'
print(word.isalpha()) # tez nie akceptuje znaków specjalnych


# isdigit - sprawdza czy wszystkie litery są cyframi
word = 'python'
print(word.isdigit())

word = '2026'
print(word.isdigit())

word = '3.14'
print(word.isdigit()) # dlatego ze zawiera .

word = '314&'
print(word.isdigit()) # dlatego ze zawiera & czyli nie przyjmuje znaków specjalnych

# isnumeric
word = '2026'
print(word.isnumeric())

word = '3.14'
print(word.isnumeric())
