####### MATCH CASE

# MATCH CASE, to stosunkowo nowa rzecz – pojawiła się w Python 3.10 (do sprawdzenia). Nie ma jej w sylabusie.
# Jest to STRUKTURA przypominająca instrukcje warunkowe, ale jest bardziej eleganckim zapisem.
# Przypomina instrukcję warunkową "if-elif" (można powiedzieć, że jest jej alternatywą).
#
# Służy do tzw. strukturalnego dopasowywania wzorców (Structural Pattern Matching).
# Używaj MATCH-CASE, gdy masz WIELE KONKRETNYCH WARTOŚCI do sprawdzenia,
# W praktyce używa się jej wszędzie tam, gdzie tradycyjne łańcuchy if-elif-else stają się zbyt rozbudowane, nieczytelne
# lub gdy chcemy sprawdzić nie tylko wartość, ale i strukturę danych (np. TYP i zawartość LISTY)
# Nie używaj MARCH-CASE, gdy operujesz na zakresach liczb "większy/mniejszy.
#
# Największą zaletą MATCH-CASE jest to, że nie tylko porównuje wartości, ale potrafi "rozpakowywać" dane
# bezpośrednio podczas sprawdzania warunku, co czyni kod bardziej czytelnym i profesjonalnym.


### STRUKTURA
#
# match <zmienna>:
#     case <wartość_1>:
#         <blok_kodu>
#     case <wartość_2>:
#         <blok_kodu>
#     case _:
#         <blok_kodu>


### PRZYKŁAD

zawod = input('Podaj mi swój zawód: ')

# Zamiast używać:

if zawod == 'programista':
    pensja = 8_000
    print(pensja)  # Wyświetl "pensja"
elif zawod == 'lekarz':
    pensja = 65_000
    print(pensja)  # Wyświetl "pensja"
elif 'nauczyciel':
    pensja = 5_000 # Wyświetl "pensja"
    print(pensja)

# Możemy użyć:

match zawod: # MATCHuj z zawód...
    case 'programista': # dla "programista"... ("case" musi być dokładnym trafieniem),
        pensja = 8_000
        print(pensja) # Wyświetl "pensja"
    case 'lekarz':
        pensja = 65_000
        print(pensja) # Wyświetl "pensja"
    case 'nauczyciel':
        pensja = 5_000 # Wyświetl "pensja"
        print(pensja)
    case _:
        print('Niestety nie znam takiego zawodu.')

# PRAKTYCZNE zastosowań instrukcji match-case:
# – Obsługa poleceń i komend tekstowych:
#   To idealne rozwiązanie dla botów (np. Discord) lub aplikacji konsolowych.
#   Pozwala na błyskawiczne dopasowanie wpisanego przez użytkownika słowa do konkretnej akcji.
#   Przykład: case "start", case "stop", case "pomoc".
#
# – Przetwarzanie kodów odpowiedzi i błędów (np. API): Zamiast wielu warunków if status == 200,
#   match-case pozwala w sposób przejrzysty obsłużyć różne scenariusze komunikacji sieciowej.
#   Zastosowanie: Rozróżnienie między sukcesem (200), błędem klienta (404) a błędem serwera (500).
#   Dopasowywanie struktur danych (Listy i Krotki): Jest to potężniejsza funkcja niż zwykłe porównanie wartości.
#   Program może sprawdzić np. czy zmienna jest listą o konkretnej długości i jednocześnie przypisać jej elementy do zmiennych.
#
# – Przykład: case [x, y] dopasuje się tylko do listy/krotki z dokładnie dwoma elementami,
#   co jest bardzo przydatne przy pracy ze współrzędnymi geograficznymi.
#   Walidacja złożonych struktur JSON / Słowników: match-case potrafi sprawdzić,
#   czy słownik posiada określone klucze o konkretnych typach wartości.
#   Jest to kluczowe w nowoczesnej analizie danych i web developmencie
#   Przykład: Sprawdzenie, czy otrzymany profil użytkownika zawiera klucz "email" i czy klucz "wiek" jest liczbą.