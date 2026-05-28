####### MATCH CASE

# MATCH CASE, to stosunkowo nowa rzecz – pojawiła się w Python 3.10 (do sprawdzenia). Nie ma jej w sylabusie.
# Jest to STRUKTURA przypominająca instrukcje warunkowe, ale jest bardziej eleganckim zapisem.
# Przypomina instrukcję warunkową "if-elif" (można powiedzieć, że jest jej alternatywą).

### STRUKTURA
#
# match <zmienna>:
#     case <wartość_1>:
#         <blok_kodu>
#     case <wartość_2>:
#         <blok_kodu>
#     .
#     .
#     .
#     case _:
#         <blok_kodu>

# Zamiast używać

if zawod == 'programista':
    pensja == 5_000
elif zawod == 'lekarz':
    pensja == 50_000

# Możemy użyć:

zawod = input('Podaj mi swój zawód: ')

match zawod: # zMATCHuj mi zawód
    case 'programista': # i dla "programista" ("case" musi być dokładnie trafiony),
        pensja = 5_000 # to pensja = 5_000
    case 'lekarz':
        pensja = 50_000
    case 'nauczyciel':
        pensja = 6_000
    case _: # Traciliśmy na "case", którego nei obsługujemy i dajemy informację
        print('Niestety nie znam takiego zawodu.')

###

wynik_matury = input('Podaj swój wynik maturalny: ')

match wynik_matury:
    case > 30: # "case" musi być dokładnym trafieniem, a nie zakresem.
        print('Nie zdałeś matury')

# DOCZYTAĆ, SPRAWDZIĆ I UZUPEŁNIĆ NOTATKI