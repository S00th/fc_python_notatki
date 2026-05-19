####### BRUDNOPIS


print('ZADANIE ')
print()
# ZADANIA:

# -> Zadanie 1 – kino
#     Użytkownik podaje swój wiek.
#     Jeśli ma mniej niż 12 lat → może obejrzeć tylko bajkę.
#     Jeśli ma od 12 do 17 lat → zapytaj, czy ma zgodę rodzica.
#     Jeśli tak → może wejść na film.
#     Jeśli nie → tylko bajka.
#     Jeśli ma 18 lub więcej → może obejrzeć dowolny film.

# age_cinema = int(input('Podaj swój wiek. '))
# zgoda_rodzica = True
#
# if 0 < age_cinema <= 12:
#     elif zgoda_rodzica:
#         print(f'Masz {age_cinema}. Czy masz zgodę rodzica?')
# else < age_cinema <=:
#     print(f'Nie masz zgody rodziców. Nie możesz bejrzećtego dilmu')
#
# print(f'Masz {age_cinema} Możesz obejrzeć tylko bajkę')
#
# if age2 >= 18: # Najpierw sprawdza wiek (tutaj następuje rozgałęzienie)
#     if has_drivers_license2: # Jeśli wiek jest >= 18, to sprawdza, czy masz prawo jazdy?
#         print(f'Jesteś pełnoletni i posiadasz prawo jazdy, więc możesz prowadzić samochód.')
#     else: # Jeśli nie masz prawa jazdy, to:
#         print(f'Jesteś pełnoletni, więc możesz zrobić prawa jazy.')
# else: # Jeśli jesteś za młody, to:
#     print(f'Jesteś za młody, aby mieć prawo jazdy')

print()
print('--------------------------------------------------------------------')
print()

print('ZADANIE 2 – Biblioteka.')
print()

# -> Zadanie 2 – biblioteka
    # Użytkownik podaje liczbę przeczytanych książek w tym miesiącu.
    # Jeśli 0 → wypisz "Musisz zacząć czytać!".
    # Jeśli od 1 do 3 → wypisz "Dobry początek".
    # Jeśli 4 lub więcej → wypisz "Super, jesteś molem książkowym!".

# books_read = float(input('Ile książek przeczytałeś w tym miesiącu? '))
#
# if books_read == 0:
#     print('Musisz zacząć czytać!')
# elif 1 <= books_read <= 3:
#     print('Dobry początek.')
# elif books_read >= 4:
#     print('Super, jesteś molem książkowym!')
# else:
#     print('Podana liczba jest mniejsza niż ZERO.')

print()
print('--------------------------------------------------------------------')
print()

print('ZADANIE 3 – Pogoda.')
print()

# -> Zadanie 3 – pogoda
    # Użytkownik wpisuje temperaturę w °C.
    # Jeśli poniżej 0 → "Mróz, ubierz czapkę".
    # Jeśli od 0 do 15 → "Chłodno, załóż kurtkę".
    # Jeśli powyżej 15 → "Ciepło, możesz iść w koszulce".

# temp = int(input('Podaj temperaturę w °C? '))
#
# if temp < 0:
#     print('Mróz – Ubierz czapkę!')
# elif 0 <= temp <= 15:
#     print('Chłodno – Załóż kurtkę')
# else:
#     print('Ciepło – Możesz iść w koszulce')

print()
print('--------------------------------------------------------------------')
print()

print('ZADANIE 4 – Zwierzę w domu.')
print()

# -> Zadanie 4 – zwierzę w domu
    # Użytkownik wpisuje, jakie ma zwierzę (pies, kot, rybka).
    # Jeśli pies → zapytaj dodatkowo, czy lubi spacery.
    # Jeśli tak → "Twój pies będzie szczęśliwy!".
    # Jeśli nie → "Pies potrzebuje ruchu!".
    # Jeśli kot → "Kot lubi drapanie i spanie".
    # Jeśli rybka → "Pamiętaj o czystej wodzie".
    # W innym przypadku → "Nie znam takiego zwierzaka".

pet = str(input('Jakie masz zwierzę? Czy jest to: pies, kot czy rybka? '))




if pet == 'pies' or 'Pies' or 'PIES':
    walk = str(input('Czy lubi spacery? (odpowiedz tak lub nie) '))
    if walk == 'tak':
        print('Twój PIES musi być bardzo szczęśliwy!')
    else:
        print('Pies potrzebuje ruchu!')
elif pet == 'kot' or 'Kot' or 'KOT':
    pat = str(input('Czy lubi drapanie i spanie? (odpowiedz tak lub nie) '))
    if pat == 'tak':
        print('Twój KOT musi być bardzo szczęśliwy!')
    else:
        print('Głąszcz go kiedy tylko możesz.')
elif pet == 'rybka' or 'Rybka' or 'RYBKA':
    water = str(input('Czy lubi drapanie i spanie? (odpowiedz tak lub nie) '))
    if water == 'tak':
        print('Twoja RYBKA musi być bardzo szczęśliwa!')
    else:
        print('Pamiętaj o czystej wodzie.')
else:
    print('Nie znam takiego zwierzaka.')

print()
print('--------------------------------------------------------------------')
print()

print('ZADANIE ')
print()

# -> Zadanie 5 – zakupy
    # Użytkownik podaje cenę produktu.
    # Za pomocą ternary operator przypisz do zmiennej status:
    # "Drogi", jeśli cena > 100,
    # "Tani", jeśli cena ≤ 100.


print()
print('--------------------------------------------------------------------')
print()

print('ZADANIE ')
print()

# =========================
# ZADANIE 1
# =========================

# Użytkownik wpisuje hasło
#
# Program ma sprawdzić:
# - czy hasło ma minimum 8 znaków
# - czy pierwszy znak NIE jest cyfrą
# - czy w haśle znajduje się znak "!" lub "?"
# - czy hasło nie zaczyna się i nie kończy tą samą literą
#
# Jeśli wszystkie warunki są spełnione:
# -> wypisz "Hasło poprawne"
#
# W przeciwnym razie:
# -> wypisz konkretny powód błędu


print()
print('--------------------------------------------------------------------')
print()

print('ZADANIE ')
print()

# =========================
# ZADANIE 2
# =========================

# Użytkownik wpisuje dowolny tekst
#
# Program ma sprawdzić:
# - czy tekst zaczyna się od "@"
# - czy kończy się liczbą
# - czy środkowy znak tekstu to litera "x"
#
# Jeśli wszystkie warunki są spełnione:
# -> wypisz "Wiadomość zaakceptowana"
#
# W przeciwnym razie:
# -> wypisz, który warunek nie został spełniony
#
# Dodatkowe utrudnienie:
# Program powinien działać również dla tekstów o parzystej długości tekstu


print()
print('--------------------------------------------------------------------')
print()

print('ZADANIE ')
print()

# =========================
# ZADANIE 3
# =========================

# Użytkownik wpisuje nick w formacie:
#
# imie#123
#
# Program ma sprawdzić:
# - czy nick zawiera dokładnie jeden znak "#"
# - czy część przed "#" ma minimum 3 znaki
# - czy część po "#" składa się wyłącznie z cyfr
# - czy numer po "#" ma dokładnie 3 cyfry
# - czy pierwsza litera nicku jest wielka
#
# Jeśli wszystko jest poprawne:
# -> wypisz "Nick poprawny"
#
# W przeciwnym razie:
# -> wypisz konkretny powód błędu