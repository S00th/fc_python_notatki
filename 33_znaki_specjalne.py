####### ZNAKI SPECJALNE

# Niektórych znaków nie będziesz w stanie wpisać w Pythonie bezpośrednio z klawiatury.
# Tego typu znaki musisz zastąpić odpowiadającemu im znakowi ucieczki (escape character), czyli \.
# Znak ucieczki zmienia interpretację znaku, który następuje bezpośrednio po nim.

# \n – Znak NOWEJ LINII w stringach
print('linia 1\nlinia 2')
print('1\n2\n3') # Wyświetl każdą liczbę w nowej linii.

# \t – Znak TABULACJI
print('linia 1 \t linia 2')

# \\ – Backslash
print(f'C:\\Users\\Nazwa')

# \" – Cudzysłów
# Ważne! Polskie cudzysłowy występują w tabeli ACSII. Nie ma potrzeby korzystać ze znaku ucieczki.
print(f'Cudzysłów zwykły: \"In the beginning was the Word\"')
print(f'Cudzysłowy polskie: „Na początku było Słowo”')

# \' – Apostrof
print(f'Harry\'ego, Google\'a')
