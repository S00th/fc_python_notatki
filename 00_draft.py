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
#
# if 0 <= age_cinema < 12:
#     print(f'Możesz obejrzeć tylko bajkę.')
# elif 12 <= age_cinema <=17:
#     parental_consent = input(f'Czy masz zgodę rodzica? (odpowiedz tak lub nie) ') # czy wpisywanie input w tym miejscu jest ok?
#     if parental_consent == 'tak':
#         print('Może wejść na film.')
#     else:
#         print(f'Możesz obejrzeć tylko bajkę.')
# elif age_cinema >= 18:
#     print(f'Może obejrzeć dowolny film.')
# else:
#     print('Podana liczba jest mniejsza niż ZERO.')


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

# pet = input('Jakie masz zwierzę? Czy jest to: pies, kot czy rybka? ')
#
# if pet == 'pies': # Co zrobić, żeby można było wpisać: pies, Pies lub PIES?
#     walk = input('Czy lubi spacery? (odpowiedz tak lub nie) ')
#     if walk == 'tak':
#         print('Twój PIES musi być bardzo szczęśliwy!')
#     else:
#         print('Pies potrzebuje ruchu!')
# elif pet == 'kot':
#     print('Głąszcz go kiedy tylko możesz.')
# elif pet == 'rybka':
#     print('Pamiętaj o czystej wodzie.')
# else:
#     print('Nie znam takiego zwierzaka.')


# Wersja rozbudowana

# pet = input('Jakie masz zwierzę? Czy jest to: pies, kot czy rybka? ')
#
# if pet == 'pies':
#     walk = input('Czy lubi spacery? (odpowiedz tak lub nie) ')
#     if walk == 'tak':
#         print('Twój PIES musi być bardzo szczęśliwy!')
#     else:
#         print('Pies potrzebuje ruchu!')
# elif pet == 'kot':
#     pat = input('Czy lubi drapanie i spanie? (odpowiedz tak lub nie) ')
#     if pat == 'tak':
#         print('Twój KOT musi być bardzo szczęśliwy!')
#     else:
#         print('Głąszcz go kiedy tylko możesz.')
# elif pet == 'rybka':
#     water = input('Często zmeiniasz jej wodę (odpowiedz tak lub nie) ')
#     if water == 'tak':
#         print('Twoja RYBKA musi być bardzo szczęśliwa!')
#     else:
#         print('Pamiętaj o czystej wodzie.')
# else:
#     print('Nie znam takiego zwierzaka.')

print()
print('--------------------------------------------------------------------')
print()

print('ZADANIE 5 – Zakupy.')
print()

# Operator trójargumentowy (ang. ternary operator), znany również jako wyrażenie warunkowe,
# to sposób na zapisanie prostej instrukcji if-else w jednej, zwięzłej linijce kodu.

# -> Zadanie 5 – zakupy
    # Użytkownik podaje cenę produktu.
    # Za pomocą TERNARY OPERATOR przypisz do zmiennej status:
    # "Drogi", jeśli cena > 100,
    # "Tani", jeśli cena ≤ 100.

# product_price = int(input('Podaj cenę produkty. '))
#
# print('Tani') if product_price <= 100 else print('Drogi')


print()
print('--------------------------------------------------------------------')
print()

print('ZADANIE 6 – Sprawdź poprawność wpisanego hasła.')
print()

# Użytkownik wpisuje hasło.
#
# Program ma sprawdzić: # mam problem ze zrozumieniem wymagań (Hasło: ma się składać z 8 znaków; zaczynać od literki; zawierać "!" i "?"; zaczynać i kończyć tym samym znakiem.)
# – czy hasło ma minimum 8 znaków
# – czy pierwszy znak NIE jest cyfrą
# – czy w haśle znajduje się znak "!" lub "?"
# – czy hasło nie zaczyna się i nie kończy tą samą literą
#
# Jeśli wszystkie warunki są spełnione:
# -> wypisz "Hasło poprawne"
#
# W przeciwnym razie:
# -> wypisz konkretny powód błędu

# password = input('Podaj hasło: ')
# correct_password = True

# if len(password) < 8:
#     print('Hasło MUSI mieć conajmniej 8 znaków.')
#     correct_password = False
# if not password[0].isdigit(): # lub not password[0].isdigit()
#     print('Pierwszy znak hasła MUSI być cyfrą.')
#     correct_password = False
# if '!' not in password and '?' not in password:
#     print('Hasło musi zawierać znak ! lub ?.')
#     correct_password = False
# if password[0] == password[-1]:
#     print('Hasło NIE może zaczyna się i kończy tym samym znakiem.')
#     correct_password = False
# if correct_password:
#     print('Hasło jest poprawne.')

print()
print('--------------------------------------------------------------------')
print()

print('ZADANIE 7 – Sprawdź poprawność wpisanego tekstu.')
print()

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

# text = input('Wpisz dowolny tekst: ')
# center = len(text) // 2
# correct_text = True
#
# if text[0] != '@':
#     print('Tekst MUSI zaczynać się od @.')
#     correct_text = False
# if text[-1].isalpha():
#     print('Tekst MUSI kończyć się liczbą.')
#     correct_text = False
# if text[center] != 'x':
#     print('Środkowym znakiem tekstu MUSI być X.')
#     correct_text = False
# if correct_text:
#     print('Wiadomość zaakceptowana.')

print()
print('--------------------------------------------------------------------')
print()

print('ZADANIE 8 – Sprawdź poprawność nicku.')
print()

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

nick = input('Wpisz NICK w formacie imię#123: ')
index_nick = nick.find("#")
correct_nick = True

if nick.count('#') != 1:
    print('Nick MISI zawierać dokładnie jeden znak #.')
    correct_nick = False
if len(nick[:index_nick]) >= 3:
    print('Przed # MUSZĄ się znaleźć przynajmniej 3 znaki.')
    correct_nick = False
if nick[index_nick+1:].isdigit():
    print('Po # mogą się znaleźć TYLKO cyfry.')
    correct_nick = False
if len(nick[index_nick+1:]) == 3:
    print('Po # MUSZĄ się znaleźć dokładnie 3 cyfry.')
    correct_nick = False
if correct_nick:
    print('Nick poprawny.')