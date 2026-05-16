# dany jest napis

napis = "Danusia jest fryzjerką i chodzi do technikum."

# na podatawie tego napisu podziel go na 2 rowne cześci – tj od początku do połwy i od połwty do końca

# przypisz do odpowiednich zmiennych

print(len(napis))
print(napis[:22])
print(napis[-1:23])

napis_lenght = len(napis)
napis_lenght_halved = napis_lenght // 2

print(napis_lenght)

print(f"To jest połowa zadania: {napis[0:napis_lenght_halved]}")
print(f"To jest druga połowa zadania: {napis[napis_lenght_halved:napis_lenght]}")

print(f"To jest połowa zadania: {napis[:napis_lenght_halved]}")
print(f"To jest połowa zadania: {napis[napis_lenght_halved:]}")

# z napisu
name = 'Bartek'
# usun literę b a następnie zamień wszystkie litery na wielkie

print(name.replace('B', '').upper())
print(name.lower().replace('b', '').upper())
print(name.replace('B', ''upper())
print(name.replace('b', '')upper())
