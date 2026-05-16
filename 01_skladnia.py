####### SKŁADNIA – Podstawowe zasady zapisu

# Na końcu linii nie stawiamy średnika. Python wie, że nowa linia to nowa instrukcja

# Komentarze / Comments: Szary tekst poprzedzony znakiem # to komentarz. Komentarze nie są częścią kodu.
# Wszystko, co napiszesz po znaku #, jest ignorowane. Komentarze do robienia notatek wewnątrz kodu
print('Cześć') # kod można przeplatać komentarzami

"# To nie jest komentarz, ponieważ tekst znajduje się w cudzysłowach"

'''Potrójne cudzysłowy (pojedyncze lub podwójne) służą do tworzenia tekstów wielolinijkowych 
(np. długich opisów lub dokumentacji funkcji).'''

# Nazwa ZMIENNEJ nie może:
    # zawierać znaków specjalnych: !, @, #, $, %, ^, &, *, (, ), -, +, =, {, }, [, ], |, \, :, ;, ", ', <, >, ,, ., ?, /, np. !Aga$
    # zawierać znaków diakrytycznych: ą, ć, ę, ł, ń, ó, ś, ź, ż, np. polskich znaków – żółć
    # zaczynać się od cyfry, np. 123_name
    # być słowem kluczowym Pythona, ani nazwą funkcji wbudowanej, np. print, if, class

print('Hello ' "World") # Możesz używać cudzysłowów pojedynczych lub podwójnych

print("a", "b", "c") # Wpisując litery, użyj cudzysłowów pojedynczych lub podwójnych
print('a', 'b', 'c') # Wpisując litery, użyj cudzysłowów pojedynczych lub podwójnych
print(1, 2, 3) # Wpisując cyfry, nie musisz używać cudzysłowów

import sys # Sprawdź, jaka jest ścieżka Pythona, przy pomocy której uruchamiamy skrypt
print(sys.executable) # wyświetl ścieżkę do Pythona, którego używam, aby uruchomić skrypt
