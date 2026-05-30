####### SKŁADNIA – Podstawowe zasady zapisu

### KOMENTARZE / Comments
#
# Szary tekst poprzedzony znakiem # to komentarz.
# Wszystko, co napiszesz po znaku # nie jest częścią kodu i jest ignorowane przez program.
# Komentarze służą do robienia notatek wewnątrz kodu.

print('Cześć') # Kod można przeplatać komentarzami

"# To nie jest komentarz, ponieważ tekst znajduje się w cudzysłowach"

'''Potrójne cudzysłowy (pojedyncze lub podwójne) służą do tworzenia tekstów wielolinijkowych 
(np. długich opisów lub dokumentacji funkcji).'''


### CUDZYSŁOWY
#
# W Pythonie możemy używać cudzysłowów podwójnych  i pojedynczych.
# Ważne, abyś zdecydował się na jeden z typów i stosował go wszędzie.
print('Hello ' "World") # Możesz używać cudzysłowów pojedynczych lub podwójnych
print("a", "b", "c")
print('a', 'b', 'c')
print(1, 2, 3) # Wpisując cyfry, nie musisz używać cudzysłowów


### ŚREDNIK
# W PYTHONIE nie stawiamy średnika na końcu linii. Python wie, że nowa linia to nowa instrukcja


# Konwencje zapisu ZMIENNYCH i KLAS
tax_rate = 0.23 # ZMIENNE i FUNKCJE nazywaj w konwencji snake_case
taxRate = 0.23 # KLASY nazywaj w konwencji CamelCase, a konkretnie lowerCamelCase
TaxRate = 0.23 # KLASY nazywaj w konwencji CamelCase, a konkretnie UpperCamelCase (nazywanej też Pascal Case)
TAX_RATE = 0.23 # STAŁE nazywaj w tej konwencja (chociaż dla Pythona STAŁE i ZMIENNE to, to samo)

EARTH_RADIUS_KM = 6397 # STAŁA (specjalny przypadek zmiennej)
PI = 3.14 # STAŁA (specjalny przypadek zmiennej)


### WCIĘCIA
#
# Python jest językiem, w którym WCIĘCIA MAJĄ ZNACZENIE.
# Nie są tylko ozdobnikiem, wskazują również, w jaki sposób będzie wykonywany program.
# Powszechnie przyjętym standardem jest WCIĘCIE będące wielokrotnością 4 SPACJI.
# Standard Python zakłada również, że zawsze używamy SPACJI, nie tabulacji.
# Dlatego też naciśnięcie <tab> w PyCharm automatycznie zmienia WCIĘCIE na 4 SPACJE.
# Jeśli chcesz wsunąć cały blok kodu (w prawo), zaznacz go i naciśnij <Tab>.
# Jeśli chcesz zmniejszyć poziom wcięcia (w lewo), naciśnij <Shift>+<Tab>.


import sys # Sprawdź, jaka jest ścieżka Pythona, przy pomocy której uruchamiamy skrypt
print(sys.executable) # wyświetl ścieżkę do Pythona, którego używam, aby uruchomić skrypt
