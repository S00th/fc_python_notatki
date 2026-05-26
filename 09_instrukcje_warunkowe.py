####### INSTRUKCJE WARUNKOWE
# #
# INSTRUKCJA WARUNKOWA if warunkowo wykonuje blok kodu.
# Podstawowa składnia (zwróć uwagę na wcięcie i dwukropek po warunku):
#
# if {warunek}:
#   {kod do wykonania linia 1}
#   {kod do wykonania linia 2}
#   {kod do wykonania linia 3}
#
# Wcięcie sygnalizuje fragment bloku, który będzie wykonany, jeśli warunek będzie spełniony.

### Warunek może być również wartością bezpośrednio logiczną:
# a = True
# b = False
# c = a or b
# if c:
#     print("Warunek prawdziwy")
#
### Co w przypadku użycia łańcucha znaków?
# c = "Przykładowy tekst"
# if c:
#     print("Ta linia zostanie wykonana")
# c = ""
# if c:
#     print("To polecenie zostanie pominięte")

# Do tej pory program wykonywał się od góry, do dołu.
#
# Podstawowe słowa kluczowe:
# if – Jeśli, to (może występować sam, ale nie ma bloku bez if) – Jeśli warunek jest spełniony, to wykonaj kod.
# else – W przeciwnym razie wykonaj inny kod (nigdy nie jest sam)
# elif – ("else if") Dodatkowe warunki do sprawdzenia (nigdy nie jest sam)
#
# SKŁADNIA
# if < condition 1 >: # Warunek zawsze zwraca BULL i w związku z tym, NIGDY nie piszemy: if condition == True:
#    do_something
# elif < condition 3 >: # Jeżeli mamy więcej niż dwie możliwości, to korzystamy z elif
#    do_something_else
# else < condition 2 >:
#    do_something_different



### ĆWICZENIE 1 – Czy użytkownik jest pełnoletni?
# Chcemy wyświetlić informację w zależności od wieku użytkownika, czy jest pełnoletni?
# Jeśli nie jest pełnoletni, czyli warunek nie został spełniony, to tedy nie rób nic i przejdź do dalszej części kodu

user_age = int(input('Podaj wiek swój wiek: ')) # input() zawsze zwraca STRING, dlatego w tym przypadku trzeba dokonać konwersji.

if user_age >= 18: # Warunek zawsze zwraca BULL
	print('Jesteś pełnoletni.')
print('Dalsza część niezależna od kodu.')



### ĆWICZENIE 2 – Czy użytkownik jest pełnoletni? Czy nie jest pełnoletni?
# Chcemy wyświetlić informację w zależności od wieku użytkownika, czy jest pełnoletni?
# Jeśli pierwszy warunek nie jest spełniony, przejdź do else.

if user_age >= 18: # Warunek zawsze zwraca BULL
	print(f'Jesteś pełnoletni i masz {user_age} lat.')
else:
    print(f'Nie jesteś pełnoletni i brakuje ci {18 - user_age} lat.')



### ĆWICZENIE 3 – Czy liczba jest podzielna przez 3?
# Pobierz od użytkownika liczbę. Sprawdź, czy jest podzielna przez trzy. Wyświetl odpowiednie komunikaty.

user_age_3 = int(input('Podaj liczbę: '))

if user_age_3 / 3: # Lub if user_are_3 % 3 == 0:
    print('Podana liczba jest podzielna przez 3.')
else:
    print('Podana liczba nie jest podzielna przez 3.')
# lub
if user_age_3 % 3:
    print('Podana liczba nie jest podzielna przez 3.')
else:
    print('Podana liczba jest podzielna przez 3.')



### ĆWICZENIE 4 – Liczba czy NIE liczba?
# Pobierz od użytkownika liczbę.
# Obsłuż sytuację, w której użytkownik pisze jakiś znak specjalny, albo literę. Uniknij błędu.

user_data = input('Podaj liczbę: ')

if user_data.isdigit():
    print(f'Podałeś liczbę: {int(user_data)}.')
else:
    print('Nie podałeś liczby.')



### ĆWICZENIE 5 – Porównaj dwie liczby.
# Przy pomocy funkcji wbudowanej input pobierz od użytkownika 2 liczby – W JEDNEJ LINII.
# Liczby oddziel od siebie przecinkiem.
# Sprawdź, czy wprowadzone liczby są sobie równe.

num_1, num_2 = input('Podaj dwie liczby (użyj , pomiędzy podanymi liczbami): ').split(',')

if int(num_1) == int(num_2):
    print(f'Liczby {num_1} i {num_2} są równe')
else:
    print(f'Liczby {num_1} i {num_2} są różne.')


### ĆWICZENIE 6 – Wiele warunków elif – Warunki ROZŁĄCZNE.
# Sprawdzenie znaku liczby – 3 możliwości – MOŻLIWY JEST TYLKO JEDEN Z 3 WARIANTÓW.
# W danym momencie może zajść tylko jedna z 3 możliwości (liczba jest dodatnia, ujemna lub róan zero).
# Warunki są ROZŁĄCZNE – tylko jedna spośród wielu możliwości może być w danym momencie spełniona.

number_3x = float(input('Podaj liczbę: '))

if number_3x > 0:
    print(f'Liczba {number_3x} jest większa od zera.')
elif number_3x < 0:
    print(f'Liczba {number_3x} jest mniejsza zera.')
else:
    print('Podana liczba to ZERO.')



### ĆWICZENIE 7 – Warunki ODDZIELNE.
# Warunki ODDZIELNE – Zachodzą w momencie, kiedy jakaś opcja spełni w danym momencie więcej niż jeden warunek.
# Inaczej mówiąc, MOŻLIWA JEST DOWOLNA LICZBA WARIANTÓW.

number_different = float(input('Podaj liczbę: '))

if number_different > 0:
    print(f'Liczba {number_different} jest dodania.')
if number_different < 0:
    print(f'Liczba {number_different} jest ujemna.')
if number_different == 0:
    print(f'Podana liczba to zero.')
if number_different % 2 == 0:
    print(f'Liczba {number_different} jest parzysta.')
if number_different % 3 == 0:
    print(f'Liczba {number_different} jest podzielna przez 3.')



### ĆWICZENIE 8 – Jakiś tekst.
# Pobierz od użytkownika jakiś tekst. Sprawdź, czy wpisał cokolwiek i wyświetl odpowiedni komunikat.
# Nie używaj operatora porównania, ani len().

jakis_tekst = input('Wpisz dowolny ciąg znaków: ')

# Zapis niżej jest uproszoną wersją: if bool(jakis_tekst):
# Nie ma też potrzeby pisania: if jakis_tekst == True:
# Wartość wpisana przez użytkownika sama w sobie przechowuje wartość logiczną.

if jakis_tekst:
    print(f'Wpisałeś {jakis_tekst}.')
else:
    print(f'Nic nie wpisałeś.')



### ĆWICZENIE 9 – ŁĄCZENIE warunków przy pomocy operatorów logicznych.
# and – Zwraca True tylko wtedy, gdy oba warunki są prawdziwe.
# or – Zwraca True, gdy przynajmniej jeden z warunków jest prawdziwy.
# not – Zaprzeczenie – zmienia True na False i odwrotnie.


# Przykład AND.
#
age = int(input('Ile masz lat ? '))
has_drivers_license = False

if age >= 18 and has_drivers_license: # Nie ma też potrzeby pisania: if age >= 18 and has_drivers_license == True:
    print(f'Jesteś pełnoletni i posiadasz prawo jazdy, więc możesz prowadzić samochód.')
else:
    print(f'Nie masz 18 lat, więc nie możesz mieć prawa jazy. Nie kłam!')
# True and False to False


# Przykład OR.
#
cash = int(input('Ile masz pieniędzy? '))
ticket_price = 4
has_ticket = False

if cash >= ticket_price or has_ticket:
    print('Możesz wejść na koncert.')
else:
    print('Nie możesz wejść na koncert')


# Przykład NOT.
# Jeśli zmienna jest logiczna, to unikamy skłądni if zalogowany == True, zamiast tego -> if zalogowany

logged_in = True
#
# # bez NOT
if logged_in: # Stosujemy wtedy, kiedy bardziej spodziewamy się, że coś się WYDARZY, niż że się NIE WYDARZY.
    print('Witaj w systemie.')
else:
    print('Musisz się zalogować.')

# z NOT
if not logged_in: # Stosujemy wtedy, kiedy bardziej spodziewamy się, że się NIE WYDARZY, niż się WYDARZY
    print('Musisz się zalogować.')
else:
    print('Witaj w systemie.')



### CIĄG WARUNKÓW i UPROSZCZENIE dotyczące przedziałów liczbowych.
# Ciąg warunków jest sprawdzany DO MOMENTU, AŻ KTÓRYŚ WARUNEK ZOSTANIE SPEŁNIONY.
# Przykładowo, jeśli spełniony będzie wiek > 0 and wiek < 10, to kolejne warunki (elif) nie będą rozpatrywane.
#
# Uproszczenie bez AND dotyczy tylko przedziałów liczbowych.
# Jeżeli dana liczba ma się mieścić pomiędzy jedną a drugą.
# Jeżeli poniżej 10 lat to dziecko.
# Jeżeli 11-17 lat to nastolatek.
# Jeżeli 18-40 lat to dorosły.
# Jeżeli 41+ lat to senior.

wiek = int(input('Podaj wiek: '))

# Zapis z AND
if wiek > 0 and wiek < 10:
    print('Jesteś dzieckiem.')
elif wiek >= 10 and wiek <= 17:
    print('Jesteś nastolatkiem.')
elif wiek >= 18 and wiek <= 40:
    print('Jesteś dorosłym.')
elif wiek > 40:
    print('Jesteś seniorem.')
else:
    print('Nie ma ujemnego wieku')

# Zapis bez AND
if 0 < wiek <= 10:
    print('Jesteś dzieckiem.')
elif 10 < wiek <= 17:
    print('Jesteś nastolatkiem.')
elif 17 < wiek <= 40:
    print('Jesteś dorosłym.')
elif wiek > 40:
    print('Jesteś seniorem.')
else:
    print('Nie ma ujemnego wieku.')



### ZAGNIEŻDŻONE warunki.
# Jeżeli mamy SEKWENCJĘ WARUNKÓW/PYTAŃ i następne pytanie ZALEŻY OD POPRZEDNIEJ ODPOWIEDZI.

liczba = int(input('Podaj liczbę: '))

if liczba > 0: # WARUNEK 1 – Czy liczba jest większa od 0? Jeśli TAK, to przejdź wiersz niżej.
    if liczba == 5: # Dodatkowo (WARUNEK 2) – Czy liczba jest równa 5? Jeśli jest równa 5...
        print('To jest 5') # ...wyświetl.
    else: # W przeciwnym razie (jeśli NIE jest równa 5)...
        print('Nie podałeś 5') # ...wyświetl.
    if liczba == 100: # Dodatkowo (WARUNEK 3) – Czy liczba jest równa 100? Jeśli jest równa 100...
        print('To jest 100') # ...wyświetl.
    else: # W przeciwnym razie (jeśli NIE jest równa 100)...
        print('Nie podałeś 100') # ...wyświetl.
else: # W przeciwnym razie (jeśli NIE jest równa 0)...
    print('Nie podałeś liczby większej niz 0') # ...wyświetl.


age2 = int(input('Ile masz lat ? '))
has_drivers_license2 = False

# # Jak działa?
if age2 >= 18: # Najpierw sprawdza wiek (tutaj następuje rozgałęzienie)
    if has_drivers_license2: # Jeśli wiek jest >= 18, to sprawdza, czy masz prawo jazdy?
        print(f'Jesteś pełnoletni i posiadasz prawo jazdy, więc możesz prowadzić samochód.')
    else: # Jeśli nie masz prawa jazdy, to:
        print(f'Jesteś pełnoletni, więc możesz zrobić prawo jazy.')
else: # Jeśli jesteś za młody, to:
    print(f'Jesteś za młody, aby mieć prawo jazdy')



### Ternary operation / Warunek w jednej linii.
# Czyli "il else" w jednej linii
# Będzie służył do przypisywania wartości warunkowo.
# Składnia: wartość_jesli_true if <warunek> else wartość_jesli_false

num11 = 11

if num11 % 2 == 0:
    wynik = 'Parzysty'
else:
    wynik = 'Nieparzysty'
print(wynik)

# Inny sposób zapisu

wynik = 'Parzysty' if num11 % 2 == 0 else 'Nieparzysty'
print(wynik)


### Warunek z NON

var = None

if not var: # Można zapisać w taki sposób
    print('Var jest puste')

if var is None:
    print('Var jest puste')  # jednak bezpieczniej jest zapisać w taki sposób.



### Operator trójargumentowy (ang. TERNARY OPERATOR)
# znany również jako wyrażenie warunkowe, to sposób na zapisanie prostej instrukcji if-else w jednej, zwięzłej linijce kodu.

# -> Zadanie – zakupy
    # Użytkownik podaje cenę produktu.
    # Za pomocą TERNARY OPERATOR przypisz do zmiennej status:
    # "Drogi", jeśli cena > 100,
    # "Tani", jeśli cena ≤ 100.

product_price = int(input('Podaj cenę produkty. '))

print('Tani') if product_price <= 100 else print('Drogi')