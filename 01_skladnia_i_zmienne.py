####### SKŁADNIA – Podstawowe zasady zapisu

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


# Python jest językiem, w którym WCIĘCIA MAJĄ ZNACZENIE.
# Nie są tylko ozdobnikiem, wskazują również, w jaki sposób będzie wykonywany program.
# Powszechnie przyjętym standardem jest WCIĘCIE będące wielokrotnością 4 SPACJI.
# Standard python zakłada również, że zawsze używamy SPACJI, nie tabulacji.
# Dlatego też naciśnięcie <tab> w Pycharm automatycznie zmienia wcięcie na 4 SPACJE (zrobi zacięcie w prawo).
# Jeśli chcesz wsunąć cały blok w edytorze, zaznacz go i naciśnij <Tab>,
# jeśli chcesz zmniejszyć poziom wcięcia, naciśnij <Shift>+<Tab>.


import sys # Sprawdź, jaka jest ścieżka Pythona, przy pomocy której uruchamiamy skrypt
print(sys.executable) # wyświetl ścieżkę do Pythona, którego używam, aby uruchomić skrypt
