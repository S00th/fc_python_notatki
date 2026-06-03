####### KONKATENACJA (złączenie) stringów

# DODAWANIE i KONKATENACJA – Czym się różnią?
#
# DODAWANIE to operacja matematyczna wykonywana na TYPACH NUMERYCZNYCH.
# Dodawanie dotyczy przede wszystkim LICZB CAŁKOWITYCH (int) oraz LICZB ZMIENNOPRZECINKOWYCH (float).
# Odbywa się przy pomocy operatora +
# Przykład:
print(2 + 2) # Wyświetli 4

# KONKATENACJA to operacja łączenia dwóch lub więcej fragmentów TESTU (string) w jeden ciąg znaków.
# TEKST (str) musi być zawsze zapisywany w cudzysłowach (pojedynczych lub podwójnych),
# pozwala to interpreterowi odróżnić go od nazw zmiennych.
# Odbywa się przy pomocy operatora +
# Przykład:
print('Cześć' + 'użytkowniku') # Wyświetli Cześćużytkowniku
print('Cześć','użytkowniku')# Wyświetli Cześću żytkowniku

# W Pythonie główna różnica między DODAWANIEM, a KONKATENACJĄ polega na TYPIE DANYCH,
# na których przeprowadzana jest operacja przy użyciu operatora +
# To, jak Python zinterpretuje ten symbol, zależy od tego, czy pracujemy na liczbach, czy na tekście.
# Ten sam operator, czyli + da zupełnie inne rezultaty dla LICZB (wynik matematyczny) i dla TEKSTU (dłuższy napis).
# Nie można bezpośrednio połączyć różnych typów danych np. TEKSTU (str) z LICZBĄ (int) za pomocą operatora +.
# Próba wykonania 'Tekst' + 404 spowoduje błąd. LICZBĘ należy najpierw zamienić na TEKST funkcją str().
#
# F-STRING
# Jest to nowoczesnym i bardzo czytelnym sposób łączenia TEKSTU ze ZMIENNĄ.
# Automatycznie dba o konwersję typów i jest uważany za styl PYTHONIC.
# Przykład:
print(f'Twoje hasło to: {password}.'))

print('1'+'1') # Dla str + str operator + działa jako operator KONKATENACJA (SKLEJENIE). – nie działa dla str + int, np. 1+'1')
print(1+1) # Dla int + int operator + działa jak operator DODAWANIA.

name = 'Aga'
last_name = 'Nowak'
age, height = 25, 180

# SPOSÓB ZAPISU 1 – Z plusem
full_text = 'Cześć! Man na imię ' + name + ' ' + last_name +'.' # zadziała tylko dla samych str
print(full_text)

# SPOSÓB ZAPISU 2 – Konwersją int na str "w locie"
full_text_numbers = 'Cześć! Man na imię ' + name + ' ' + last_name + '. ' 'Mam ' + str(age) + ' lat ' 'i ' + str(height) + ' wzrostu.'
print(full_text_numbers)

# SPOSÓB ZAPISU 3 – F-string rounding (nowoczesna metoda konkatenacji stringów, przy której nie musimy martwić się o typ)
# dodatkowo pozwala nam zaokrąglać wyniki działań – f'Cześć! Man na imię {Ada} i mam {height:.2f} cm wzrostu.")
full_text_f = f'Cześć! Man na imię {name} {last_name}. Mam {age} lat i {height} wzrostu.'
print(full_text_f)

print('Hello' + ' ' + 'World') # Łańcuchy znaków możemy łączyć za pomocą operatora +, przykładowo:
print('Hello ' * 5) # Możemy też powtórzyć wybrany tekst kilkukrotnie za pomocą operatora * (tutaj wyświetlimy 'Hello' pięć razy)


####### METODY STRINGÓW – Pozwalają modyfikować TEKST.
#
# Na razie przyjmujemy, że FUNKCJE i METODY różnią się jedynie składnią.
# METODY są nierozerwalnie związane z konkretnym TYPEM DANYCH lub OBIEKTEM.
# Wywołuje się je "na rzecz" konkretnego OBIEKTU, używając zapisu z kropką (np. nazwa_listy.append())
# FUNKCJA nazywana jest METODA dlatego, że odnosi się do konkretnego ELEMENTU (np. listy), na której jest wywołana.
#
# Wywołanie FUNKCJI (FUNKCJA wywołuje lub zwraca)
# Zapis FUNKCJI
# funkcja(argument1, argument2)
#
# Wywołanie METODY
# Zapis METODY
# obiekt.metoda(argument1, argument2)



####### INDEKSOWANIE i SLICING stringów
# Z każdego napisu możemy wziąć pojedynczą literę lub część liter.

# INDEKSOWANIE – to wycinanie jednego znaku ze STRINGA.

# Każda litera w napisie ma swój INDEX (jak niżej).
# INDEX, to adres litery w tekście (SPACJE też podlegają indeksowaniu).
# Możemy indeksować od LEWEJ do PRAWEJ, ale też od PRAWEJ do LEWEJ.
# Python jest językiem indeksowanym od ZERA, co znaczy, że pierwszy element STRINGA lub KOLEKCJI (od lewej) to ZERO.
# Natomiast ostatni element (pierwszy od końca) to -1.
# Jeżeli wskazany INDEX nie istnieje, to zostanie podniesiony błąd IndexError.
# Jeżeli wskażemy nieistniejący lub częściowo nieistniejący ZAKRES, to nie dostaniemy błędu.
# INDEX nie może być floatem (musi być integerem)

#  D  W  A     S  Ł  O  W  A
#  0  1  2  3  4  5  6  7  8    od LEWEJ > do PRAWEJ
# -9 -8 -7 -6 -5 -4 -3 -2 -1    od PRAWEJ < do LEWEJ

# Dla pierwszego znaku od LEWEJ będzie to [0], dla drugiego [1], dla trzeciego [2] itd.
# Dla pierwszego znaku od PRAWEJ będzie to [-1], dla drugiego [-2], dla trzeciego [-3] itd.

# Składnia/Syntax -> string[index]

jakis_napis = 'abcdefghijksdkjhfkdjshfkjdhsfkjdhfsddd12214'

print(f'Pierwsza litera napisu {jakis_napis} to {jakis_napis[0]}') # W {} wpisujemy nazwę zmiennej, a w [0] wartość znaku, o który nam chodzi.
print(f'Druga litera napisu {jakis_napis} to {jakis_napis[1]}')
print(f'OSTATNIA litera napisu {jakis_napis} to {jakis_napis[-1]}') # Indeks -1 to zawsze ostatni element
print(f'Index, którego nie ma w napisie {jakis_napis} to {jakis_napis[1000]}') # Wyświetli błąd IndexError



####### SLICING – to wycinanie fragmentu/kilku znaków ze STRINGA
#
# SKŁADNIA
# iterable[start_index: stop_index: step] / zmienna[start:end:step]
#
# Gdzie: start_index – included – domyślnie index 0
# Gdzie: stop_index – excluded – domyślnie ostatni
# Gdzie: step – domyślnie 1 – 1 oznacza "Weź każdą literę (po kolei)", 2 "Weź co drugą literę (po kolei)", a -1 "Weź każdą literę (w odwróconej kolejności)".

jakis_inny_napis = 'Język Python można wykorzystać do modelowania sieci neuronowych'

print(jakis_inny_napis[0:5]) # Weź litery od indeksu 0 do indeksu 5 [0:5], ale bez 5 (piąty znak indeksu jest wyłączona), krok (brak)
print(jakis_inny_napis[:5]) # Jak powyżej, bo start_indeks domyślnie 0 (czyli od początku do 5, ale bez 5)
print(jakis_inny_napis[0+1:5-1]) # Weź litery od indeksu 1 (0+1) do indeksu 4 (5-1), ale bez 5 (piąty znak indeksu jest wyłączona), krok (brak)
print(jakis_inny_napis[14:30:2]) # Weź litery od indeksu 14 do 30, bez 30, co druga literę.
print(jakis_inny_napis[-11:]) # Weż wszystkie litery od -11 od końca do końca
print(jakis_inny_napis[-11::2]) # Weź wszystkie litery od -11 od końca do końca, co druga litera
print(jakis_inny_napis[::]) # Weź cały tekst – dokładnie jak print(jakis_inny_napis)
print(jakis_inny_napis[::-1]) # Weź cały tekst od tyłu
print(jakis_inny_napis[4::-1]) # UWAGA! Prosząc o wyraz zapisany od tyłu, wpisujemy przedział patrząc od tyłu (od 5 znaku do 0).

file = 'raport_finansowy_2026_final.csv'
print(f'Trzy ostatnie znaki przed kropką to: {file[file.find('.')-3:file.find('.')]}') # Weź 3 ostatnie znaki przed kropką.

# Jeżeli wskażemy nieistniejący lub częściowo nieistniejący ZAKRES, to nie dostaniemy błędu.
print(jakis_inny_napis[30: 100]) # Wypisze tyle, ile jest.
print(jakis_inny_napis[1_000: 10_000]) # Nic nie wypisze, bo przedział całkiem poza zakresem.

# Sprawdzanie parzystość jakiejś zmiennej (czy liczba jest podzielna przez 2): zmienna % 2 == 0

### ĆWICZENIE – Udowodnij, że słowo oko jest palindromem a słowo koparka nim nie jest

word_oko = 'oko'
word_koparka = 'koparka'

print(word_oko)
print(word_oko[::-1] == word_oko)

print(word_koparka)
print(word_koparka[::-1] == word_koparka)

###

# Długość każdego obiektu iterowalnego można zmierzyć przy pomocy FUNKCJI wbudowanej len().
print(f"Długość napisu {jakis_inny_napis} to {len(jakis_inny_napis)}")

# ĆWICZENIE – Znalezienie indeksu środkowego
# Na podstawie tego napisu podziel go na dwie, równe części – tj. od początku do połowy i od połowy do końca.
# Przypisz do odpowiednich zmiennych.

napis = "Danusia jest fryzjerką i chodzi do technikum."
napis_lenght = len(napis)
napis_lenght_halved = napis_lenght // 2 # Znalezienie indeksu środkowego, chcemy LICZBY całkowitej, więc stosujemy //

print(f"To jest połowa zadania: {napis[:napis_lenght_halved]}")
print(f"To jest druga połowa zadania: {napis[napis_lenght_halved:]}")



####### METODY stringów

sentence1 = 'dzisiaj JEST wtorek. a jutro będzie ŚRODA'
day = 'poniedziałek, wtorek, środa'

# print(day.upper())
# print(day.lower())
# print(day.title())

print(sentence1.upper()) # Zwraca całe wyrażenie WIELKIMI literami.
print(sentence1.lower()) # Zwraca całe wyrażenie małymi literami.
print(sentence1.title()) # Każde słowo w wyrażeniu zaczyna się od wielkiej litery.
print(sentence1.capitalize()) # Tylko pierwsza litera, pierwszego wyrazu w wyrażeniu jest WIELKA.

# Wartość zwracana dotyczy zarówno METODY, jak i FUNKCJI.
# Kiedy już wywołamy FUNKCJĘ albo METODĘ (na stringu), to też otrzymamy string, ale zmodyfikowany.
# Jednak nie wszystkie metody będą zwracały string.



####### strip() – Usunięcie białych znaków z początku tekstu i z końca

sentence = '   uczymy się Pythona       '
clean_sentence = sentence.strip() # Usunięcie białych znaków z początku tekstu i z końca
# lstrip() – Usuń znaki z początku (od lewej),
# rstrip() – Usuń znaki z końca napisu (od prawej).

print(sentence)
print(sentence.strip())
print(sentence.lstrip())
print(sentence.rstrip())

print(len(sentence)) # Wyświetl liczbę znaków w zdaniu – działanie bez strip() – czyli policz ze SPACJAMI
print(len(clean_sentence)) # Wyświetl liczbę znaków w zdaniu – działanie ze strip() – czyli policz bez SPACJI



####### replace(old, new) - Zmienia fragment tekstu na inny.
# UWAGA! 90% operacji wykonywanych na tekście w Pythonie, to ZAMIANA TEKSTU !!!
# Jeśli chcemy usunąć znak, to musimy zamienić znak na NIC – nie ma metody REMOVE.
# Wielkość znaku ma znaczenie (metoda jest "case sensitive")

word = 'potop'
print(word.replace('p', 'c')) # Zamień wszystkie litery 'p' na 'c'.
print(word.replace('p', '')) # Zamień wszystkie litery 'p' na '' – czyli w praktyce USUŃ znak.


# ĆWICZENIE – Usuń literę 'b', a następnie zamień wszystkie litery na wielkie.

name = 'Bartek'

name_lower = name.lower()
name_final = name_lower.replace('b','')
print(name_final.upper())

# Niżej – zapis w formie METHODS CHAINING / Łańcuchowe wywoływanie metod (wyżej – bez METHODS CHAINING)
# W zwykłej metodzie musimy przechować wynik w pamięci, żeby móc go wykorzystać w kolejnym kroku, co zużywa więcej pamięci.
# METHODS CHAINING oszczędza miejsce w pamięci i zajmuje mniej miejsca w kodzie.

print(name.lower().replace('b', '').upper())

# METHODS CHAINING – możemy zapisać ciąg, w kilku linijkach, dzieląc go \
# Zapis w takiej formie zwiększa czytelność kodu

name_final2 = name.lower()\
    .replace('b', '')\
    .upper()
print(name_final2.upper())



####### split(sep) –  Zwraca listę stringów !!!!!!!!!!!!!!
# Jeśli mamy ustrukturyzowany tekst, gdzie każdy z elementów jest oddzielony od siebie tym samym separatorem:
# np. names = 'basia,danusia,asia,bartek,ania'
# to możemy wyciągnąć każdy z elementów osobno.
# split będzie miał argument separatora, np. dla przykłady wyżej split(',')

names = 'basia, danusia, asia, bartek, ania'
print(names.split(', ')) # separatorem jest przecinek i spacja

languages = 'python|java|csharp|js'
print(languages.split('|'))

import os
print(os.getcwd()) # Wypisz ścieżkę roboczą, w której aktualnie pracujemy (Get Current Working Directory) – w tym przypadku Y:/Py/FC/FC_kurs.
print(os.getcwd().split("\\")) # Zwróć string ze ścieżki
# Wyodrębnij każdy element ścieżki, jako osobny element listy (czyli: ['Y:', 'Py', 'FC', 'FC_kurs'])
# UWAGA! Pojedynczy \ służy do tworzenia znaków specjalnych (np. \n lub \t)
# Aby powyższy kod zadziałał, musimy jakby stworzyć znak specjalny \ (DOPYTAĆ !!!)

# split() w połączeniu z input() pozwala też na wyciągnięcie kilku danych od użytkownika – zapis w JEDNYM WIERSZU.
num_1, num_2 = input('Podaj dwie liczby – użyj , między liczbami: ').split(',')



####### join() – Złączenie kolekcji typu LISTA w pojedynczy STRING !!!!!!!!!!!!!!
# Jest odwrotnością split()
# Zwróć listę osobnych stringów wrzucaną w jeden string.

lang_list = ['python', 'java', 'csharp', 'js']

joined_string = ', '.join(lang_list)
print(joined_string)
# UWAGA! Metoda join() ma specyficzną składnię: 'separator, którym chcemy oddzielić wartości z listy'.join(name)
# np. dla: '#'.join(lang_list) otrzymamy: python#java#csharp#js



####### find() - Zwraca INDEKS znaku
# Zwraca INTEGER (indeks jest zawsze liczbą całkowitą).
# Jeżeli metoda nie znajdzie szukanego znaku lub ciągu znaków, zwraca wartość -1 (nie mylić z ostatnim indeksem).
# Pozwala to na bezpieczne sprawdzenie wyniku bez przerywania działania programu (np. za pomocą instrukcji if).

word = 'python'
print(word.find('p')) # Znak występuje w słowie, więc poda indeks znaku – w tym przypadku 0
print(word.find('w')) # Znak nie występuje w słowie, więc wyświetli -1

sentence = "python jest super"
print(sentence.find('e')) # Zwraca tylko pierwsze wystąpienie literki e (w zdaniu znajdują się dwie literki 'e')
print(sentence.find('es')) # Można też wskazać fragment tekstu, aby sprawdzić, gdzie się on zaczyna

product_code = 'LAPTOP-DELL-2026-PRO'
przerwa1 = product_code.find('-') # Zwróć index pierwszego wystąpienia znaku -
przerwa2 = product_code.find('-', przerwa1 +1) # Zwróć index drugiego wystąpienia znaku -



####### index() – Wyszukaj. Działa jak find(), ale jeśli nie znajdzie, to podnosi BŁĄD
# Jeżeli szukany element nie zostanie odnaleziony, metoda ta zgłasza błąd (wyjątek ValueError).
# Powoduje to natychmiastowe zatrzymanie programu, chyba że programista zastosuje odpowiednią obsługę błędów (np. blok try-except).

sentence = "python jest super"
print(sentence.index('super'))



####### count() – Zwraca liczbę wystąpień, a jeśli nie znajdzie, wyświetli ZERO.
# Zwraca INTEGER (liczba wystąpień jest zawsze liczbą całkowitą).

sentence = "python jest super"
print(sentence.count('p')) # Zwróć, ile liter p występuje w tekście.
print(sentence.count('x')) # Zwróć, ile liter x występuje w tekście – tutaj zwróci 0, ponieważ w tekście nia występuje x.



####### startswith() - Sprawdza, czy dany napis ZACZYNA SIĘ od danego prefiksu !!!!!!!!!!!!!!
# Zwraca bool

word = 'python'

print(word.startswith('p')) # Czy wyraz python zaczyna się na p
print(word.startswith('y')) # Czy wyraz python zaczyna się na x

print(word.startswith('py')) # Czy wyraz python zaczyna się na pic
print(word.startswith('hon')) # Czy wyraz python zaczyna się na pyt



####### endswith() – Sprawdza, czy dany napis KOŃCZY SIĘ danym suffixem.
# Zwraca BOOL

file = 'data.csv'
print(file.endswith('csv')) # Czyli czy nazwa pliku koczy się na wyraz csv (czyli czy rozszerzenie pliku to .csv)
print(file.endswith('.csv'))
print(file.endswith('ta'))


### ĆWICZENIE – Dana jest nazwa pliku
# Bez użycia metody endswith(), sprawdź czy jest rozszerzenia .xlsx.

filename = 'tabela.xlsx'
print(filename[-5:] == '.xlsx')



####### isaplha() - Sprawdza czy wszystkie znaki są LITERAMI alfabetu
# Zwraca BOOL

word = 'python'
print(word.isalpha()) # True, bo składa się z liter alfabetu

word = 'python123'
print(word.isalpha()) # False, bo string zawiera napisy, które nie są literami

word = 'python@.'
print(word.isalpha()) # False, bo nie akceptuje znaków specjalnych




####### isdigit() – Sprawdza czy wszystkie znaki są CYFRAMI całkowitymi.
# Zwraca BOOL
# Obejmuje cyfry od 0 do 9.
# Rozpoznaje niektóre znaki specjalne, które są technicznie cyframi, np. indeksy górne i dolne ².
# NIE akceptuje znaków reprezentujące wartości liczbowe w standardzie Unicode, takich jak UŁAMKI zapisanych w formie ½.
# NIE akceptuje znaków liczbowych z innych systemów pisma np. 三 (japońskie 3).

word1, word2, word3, word4, word5, word6, word7 = '2026', 'python', '3.14', '314&', '²', '½', '三'
print(word1.isdigit()) # True, bo składa się z cyfr
print(word2.isdigit()) # False, bo składa się z liter alfabetu
print(word3.isdigit()) # False, bo nie akceptuje .
print(word4.isdigit()) # False, bo nie akceptuje znaków specjalnych
print(word5.isdigit()) # True, bo rozpoznaje indeks górny ² i dolny ₂
print(word6.isdigit()) # False, bo nie rozpoznaje ułamków zapisanych w formie ½ (Unicode)
print(word7.isdigit()) # False, bo nie akceptuje liczb z innych systemów pisma np. 三 (japońskie 3).



####### isnumeric() – Sprawdza czy wszystkie znaki są CYFRAMI całkowitymi.
# Zwraca BOOL
# Obejmuje cyfry od 0 do 9.
# Rozpoznaje niektóre znaki specjalne, które są technicznie cyframi, np. indeksy górne i dolne ².
# Akceptuje inne znaki reprezentujące wartości liczbowe w standardzie Unicode, takie jak UŁAMKI zapisanych w formie ½.
# Akceptuje znaki liczbowe z innych systemów pisma np. 三 (japońskie 3).

word1, word2, word3, word4, word5, word6, word7 = '2026', 'python', '3.14', '314&', '²', '½', '三'
print(word1.isnumeric()) # True, bo składa się z cyfr
print(word2.isnumeric()) # False, bo składa się z liter alfabetu
print(word3.isnumeric()) # False, bo nie akceptuje .
print(word4.isnumeric()) # False, bo nie akceptuje znaków specjalnych
print(word5.isnumeric()) # True, bo rozpoznaje indeks górny ² i dolny ₂
print(word6.isnumeric()) # True, bo rozpoznaje ułamki zapisane w formie ½ (Unicode)
print(word7.isnumeric()) # True, bo rozpoznaje liczb z innych systemów pisma np. 三 (japońskie 3).


# UWAGA! Różnica między metodami insumeric() i isdigit() polega na zakresie znaków, które uznają za „liczbowe”.

# Jeśli chcesz sprawdzić, czy tekst wpisany przez użytkownika można bezpiecznie zamienić na liczbę całkowitą (int),
# najbezpieczniej jest użyć metody .isdigit().

# Rzutowanie na int() tekstu, który zawiera ułamek ½ spowodowałoby błąd programu,
# mimo że isnumeric() zwróci dla niego prawdę.

# isdigit() używaj przy walidacji danych wejściowych w prostych programach.
# isnumeric() używaj pracując z bardziej egzotycznymi zestawami znaków (np. pracując z cyframi w języku japońskim).



# Najczęściej wykorzystywane METODY stringów to:
# – split()
# – strip()
# – join()
# – replace()
# – startswith()