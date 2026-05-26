####### SKŁADNIA – Podstawowe zasady zapisu

# Zmienne (Variables) można wyobrazić sobie jako pudełka, w których przechowywane sę różne informacje.
# Umożliwiają one zapisać dane (np. liczbę lub tekst), nadać im nazwę i wracać do nich w dalszej części swojego programu.
# Zrozumienie zmiennych to fundament, na którym zbudujesz całą swoją wiedzę o programowaniu.
# zmienna = wartość
# NAZWA zmiennej znajduje się zawsze po lewej stronie znaku równości,
# po prawej stronie znajduje się jej WARTOŚĆ.
# Nazwa zmiennej MOŻE składać się z dużych i małych liter alfabetu łacińskiego, cyfr, oraz znaku "_".

# Nazwa ZMIENNEJ nie może:
    # zawierać SPACJI
    # zawierać znaków specjalnych: !, @, #, $, %, ^, &, *, (, ), -, +, =, {, }, [, ], |, \, :, ;, ", ', <, >, ,, ., ?, /, np. !Aga$
    # zawierać znaków diakrytycznych: ą, ć, ę, ł, ń, ó, ś, ź, ż, np. polskich znaków – żółć
    # zaczynać się od cyfry, np. 123_name
    # być słowem kluczowym Pythona, ani nazwą funkcji wbudowanej, np. print, if, class

# W PYTHONIE nie stawiamy średnika na końcu linii. Python wie, że nowa linia to nowa instrukcja
#
# Komentarze / Comments: Szary tekst poprzedzony znakiem # to komentarz. Komentarze nie są częścią kodu.
# Wszystko, co napiszesz po znaku #, jest ignorowane. Komentarze do robienia notatek wewnątrz kodu
print('Cześć') # kod można przeplatać komentarzami

"# To nie jest komentarz, ponieważ tekst znajduje się w cudzysłowach"

'''Potrójne cudzysłowy (pojedyncze lub podwójne) służą do tworzenia tekstów wielolinijkowych 
(np. długich opisów lub dokumentacji funkcji).'''


print('Hello ' "World") # Możesz używać cudzysłowów pojedynczych lub podwójnych
print("a", "b", "c")
print('a', 'b', 'c')
print(1, 2, 3) # Wpisując cyfry, nie musisz używać cudzysłowów

import sys # Sprawdź, jaka jest ścieżka Pythona, przy pomocy której uruchamiamy skrypt
print(sys.executable) # wyświetl ścieżkę do Pythona, którego używam, aby uruchomić skrypt
