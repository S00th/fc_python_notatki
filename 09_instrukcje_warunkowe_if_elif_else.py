####### INSTRUKCJE WARUNKOWE
#
# INSTRUKCJA WARUNKOWA if warunkowo wykonuje blok kodu znajsujący się po dwukropku, w wierszach niżej, po zacięciu.
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
#
# tekst = "Przykładowy tekst."
# if tekst:
#     print("Ta linia zostanie wykonana")
# tekst = ""
# if tekst:
#     print("To polecenie zostanie pominięte")

# Do tej pory program wykonywał się od góry, do dołu.
#
# Podstawowe słowa kluczowe:
# if – Jeśli, to (może występować sam, ale nie ma bloku bez if) – "Jeśli warunek jest spełniony, to wykonaj kod".
# else – "W przeciwnym razie wykonaj inny kod" (else nigdy nie jest sam)
# elif – ("else if") Dodatkowe warunki do sprawdzenia (elif nigdy nie jest sam)
#
# SKŁADNIA
# if < condition 1 >: # WARUNEK zawsze zwraca BULL i w związku z tym, NIGDY nie piszemy: if condition == True:
#    do_something
# elif < condition 3 >: # Jeżeli mamy WIĘCEJ NIŻ DWIE MOŻLIWOŚCI, to korzystamy z "elif"
#    do_something_else
# else < condition 2 >: # Jeżeli mamy TYLKO DWIE MOŻLIWOŚCI, to korzystamy z "if" oraz "else"
#    do_something_different



### ĆWICZENIE – Czy użytkownik jest pełnoletni?
# – Jeżeli użytkownik jest pełnoletni, wyświetl: "Jesteś pełnoletni".
# – Jeżeli użytkownik nie jest pełnoletni, wyświetl: "Nie jesteś pełnoletni".

user_age = int(input('Podaj wiek swój wiek: ')) # input() zawsze zwraca STRING, dlatego w tym przypadku trzeba dokonać konwersji.

if user_age >= 18:
    print('Jesteś pełnoletni.') # Wcięcie decyduje o tym, jakie polecenia zostaną wykonane, kiedy nasze wyrażenie z wiersza nad wcięciem będzie prawdziwe.
else:
    print(f'Nie jesteś pełnoletni')

# Dodatkowo. Jeśli użytkownik nie jest pełnoletni, wyświetl informację ile brakuje mu do 18ki.
# – Nie jesteś pełnoletni i brakuje ci XXX lat.

if user_age >= 18:
    print(f'Jesteś pełnoletni i masz {user_age} lat.')
else:
    print(f'Nie jesteś pełnoletni i brakuje ci {18 - user_age} lat.')



### ĆWICZENIE – Co jest stolicą Polski?
# – Jeżeli użytkownik poda prawidłowo stolicę Polski, wyświetl: "Tak. Warszawa jest stolicą polski.".
# – Jeżeli użytkownik nie poda prawidłowo stolicę Polski: "XXX nie jest stolicą Polski.".
# – Program ma działać bez względu na to jakimi literkami (dużymi czy małymi), użytkownik wpisał nazwę stolicy
# – Wyświetl nazwę miasta-odpowiedzi, zaczynającą się od wielkiej literki, a pozostałę litermi mają być małe.

stolica = input('Jakie miasto jest stolicą Polski? ')

if stolica.lower() == 'warszawa': # Uwaga 1
    print('Tak. Warszawa jest stolicą polski.')
else:
    print(f'{stolica.capitalize()} nie jest stolicą Polski.') # Uwaga 2

# 1. Dzięki .lower() każde wpisane "WARSZAWA", "Warszawa", "wArSzAwA" zostanie zamienione PRZED porównaniem go do "warszawa".
# 2. Dzięki .capitalize() wyświetlony wyraz zawsze będzie zaczynał się od wielkiej litery.


### ĆWICZENIE 3 – Czy liczba X jest podzielna przez 3?
# – Pobierz od użytkownika liczbę.
# – Sprawdź, czy jest podzielna przez trzy i wyświetl odpowiednie komunikaty.

number = int(input('Podaj liczbę: '))

if number % 3 == 0:  # WARUNEK mówi: jeżeli NUMBER podzielony przez 3 NIE MA reszty z dzielenia (reszta wynosi 0), to będzie to PRAWDA.
    print(f'Liczba {number} jest podzielna przez 3.') # W związku z tym wyświetl "Liczba JEST podzielna przez 3".
else:
    print(f'Liczba {number} nie jest podzielna przez 3')

# inny zapis

if number % 3:  # WARUNEK mówi: jeżeli NUMBER podzielony przez 3 MA resztę z dzielenia (reszta wynosi 1), to będzie to FAŁSZ.
    print(f'Liczba {number} nie jest podzielna przez 3') # W związku z tym wyświetl "Liczba NIE JEST podzielna przez 3".
else:
    print(f'Liczba {number} jest podzielna przez 3.')



### ĆWICZENIE – Liczba czy NIE liczba?
# Pobierz od użytkownika liczbę.
# Obsłuż sytuację, w której użytkownik pisze jakiś znak specjalny, albo literę. Uniknij błędu.

user_data = input('Podaj liczbę: ')

if user_data.isdigit():
    print(f'Podałeś liczbę: {int(user_data)}.')
else:
    print('Nie podałeś liczby.')



### ĆWICZENIE – Porównaj dwie liczby.
# Przy pomocy funkcji wbudowanej input pobierz od użytkownika 2 liczby – W JEDNEJ LINII.
# Liczby oddziel od siebie przecinkiem.
# Sprawdź, czy wprowadzone liczby są sobie równe.

num_1, num_2 = input('Podaj dwie liczby – użyj , między liczbami: ').split(',')

if int(num_1) == int(num_2):
    print(f'Liczby {num_1} i {num_2} są równe')
else:
    print(f'Liczby {num_1} i {num_2} są różne.')



####### Warunki ROZŁĄCZNE – możliwy jest TYLKO JEDEN Z WARIANTÓW (wiele warunków elif). !!!!!!!!!!!!!!!!!!

### ĆWICZENIE – wiele warunków elif
# Sprawdzenie znaku liczby – 3 możliwości – MOŻLIWY JEST TYLKO JEDEN Z 3 WARIANTÓW.
# W danym momencie może zajść tylko jedna z 3 możliwości (liczba jest dodatnia, ujemna lub równa zero).
# Warunki są ROZŁĄCZNE – tylko jedna spośród wielu możliwości może być w danym momencie spełniona.

num3x = float(input('Podaj liczbę: '))

if num3x > 0:
    print(f'Liczba {num3x} jest większa od zera.')
elif num3x < 0:
    print(f'Liczba {num3x} jest mniejsza zera.')
else:
    print('Podana liczba to ZERO.')

# lub – DOPYTAĆ czy mogę użyć 2x elif i nie użyć else !!!!!!!!!!!!!!!!!!

if num3x < 0:
    print(f'Liczna {num3x} jest mniejsza od ZERA.')
elif num3x > 0:
    print(f'Liczba {num3x} jest większa od ZERA.')
elif num3x == 0:
    print('Podana liczba to ZERO.')



####### Warunki ODDZIELNE – kiedy możliwa jest DOWOLNA LICZBA WARIANTÓW (wiele warunków if).
#
#### ĆWICZENIE
# Warunki ODDZIELNE – Zachodzą w momencie, kiedy jakaś opcja spełni w danym momencie więcej niż jeden warunek.

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



### ĆWICZENIE – Jakiś tekst.
# Pobierz od użytkownika jakiś tekst. Sprawdź, czy wpisał cokolwiek i wyświetl odpowiedni komunikat.
# Nie używaj operatora porównania, ani len().

jakis_tekst = input('Wpisz dowolny ciąg znaków: ')

if jakis_tekst:
    print(f'Wpisałeś {jakis_tekst}.')
else:
    print(f'Nic nie wpisałeś.')

# Zapis niżej jest uproszoną wersją: if bool(jakis_tekst):
# Nie ma też potrzeby pisania: if jakis_tekst == True:
# WARTOŚĆ wpisana przez użytkownika sama w sobie PRZECHOWUJE WARTOŚĆ LOGICZNĄ.



####### ŁĄCZENIE warunków przy pomocy operatorów logicznych.
# and – Zwraca True tylko wtedy, gdy oba warunki są prawdziwe.
# or – Zwraca True, gdy przynajmniej jeden z warunków jest prawdziwy.
# not – Zaprzeczenie – zmienia True na False i odwrotnie.


### ĆWICZENIE
# ŁĄCZENIE warunków przy pomocy operatorów logicznych – przykład AND

age = int(input('Ile masz lat: '))
has_drivers_license = True

if age >= 18 and has_drivers_license: # Nie ma też potrzeby pisania: if age >= 18 and has_drivers_license == True:
    print('Masz 18 lat i posiadasz prawo jazdy')
else:
    print(f'Nie masz 18 lat. Brakuje ci {18 - age} lat.')


# ŁĄCZENIE warunków przy pomocy operatorów logicznych – przykład OR
#
cash = int(input('Ile masz pieniędzy? '))
ticket_price = int(input('Ile kosztuje bilet? '))
ticket = False

if cash >= ticket_price or ticket:
    print('Możesz wejść do kina')
else:
    print('Nie możesz wejść do kina')



# ŁĄCZENIE warunków przy pomocy operatorów logicznych – przykład NOT
#
# Jeżeli zmienna jest logiczna, to unikamy składni: if zalogowany == True
# zamiast tego użyj: if zalogowany

logged_in = True

# bez NOT
if logged_in: # Stosujemy, kiedy bardziej spodziewamy się, że coś się WYDARZY, niż że się NIE WYDARZY.
    print('Witaj w systemie.')
else:
    print('Musisz się zalogować.')

# z NOT
if not logged_in: # Stosujemy, kiedy bardziej spodziewamy się, że się NIE WYDARZY, niż się WYDARZY
    print('Musisz się zalogować.')
else:
    print('Witaj w systemie.')



### CIĄG WARUNKÓW i UPROSZCZENIE dotyczące przedziałów liczbowych.
#
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

# Zapis z "and"

if wiek > 0:
    if wiek <= 10:
        print('Jesteś dzieckiem.')
elif wiek > 10 and wiek <= 17:
    print('Jesteś nastolatkiem.')
elif wiek > 17 and wiek <= 40:
    print('Jesteś dorosły.')
elif wiek > 40:
    print('Jesteś seniorem.')
else:
    print('Nie możesz mieć tyle lat.')

# Zapis bez AND – UPROSZCZENIE dotyczące przedziałów liczbowych.

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



####### Warunki ZAGNIEŻDŻONE
# Polegają na umieszczanie jednej instrukcji warunkowej (np. "if") wewnątrz innej instrukcji warunkowej.
# Pozwalają na tworzenie wielopoziomowej logiki, w której kolejny warunek jest SPRAWDZANY tylko wtedy, gdy poprzedni został spełniony.
# Stasujemy, kiedy SEKWENCJĘ WARUNKÓW i następne pytanie ZALEŻY OD POPRZEDNIEJ ODPOWIEDZI.

# Przykład – Wiek i prawo jazdy

age2 = int(input('Ile masz lat ? '))
has_drivers_license2 = True

if age2 >= 18: # WARUNEK 1 – Jeżeli masz 18 lat, to... przejdź wiersz niżej (tutaj następuje rozgałęzienie)
    if has_drivers_license2: # WARUNEK 2 – Jeżeli masz prawo jazdy, to...
        print('Jesteś pełnoletni i posiadasz prawo jazdy, więc możesz prowadzić samochód.')
    else: # W przeciwnym razie (jeżeli NIE masz prawa jazdy)...
        print('Jesteś pełnoletni, więc możesz zrobić prawo jazy.')
else: # W przeciwnym razie (jeśli NIE masz 18 lat)...
    print(f'Jesteś za młody. Możesz zrobić prawo jazdy za {18 - age2} lat.')

# Przykład – LICZBA

liczba = int(input('Podaj liczbę: '))

if liczba > 0: # WARUNEK 1 – Jeżeli liczba jest większa od 0, to... przejdź wiersz niżej.
    if liczba > 5: # WARUNEK 2 – Jeżeli liczba jest większa od 5, to...
        print(f'Liczba {liczba} jest większa niż 5.') # ...wyświetl.
    else: # W przeciwnym razie (jeśli NIE jest większa od 5)...
        print(f'Liczba {liczba} jest mniejsza niż 5.') # ...wyświetl.
    if liczba > 10: # WARUNEK 3 – Jeżeli liczba jest większa od 10, to...
        print(f'Liczba {liczba} jest większa niż 10') # ...wyświetl.
    else: # W przeciwnym razie (jeśli NIE jest większa od 10)...
        print(f'Liczba {liczba} jest mniejsza niż 10') # ...wyświetl.
else: # W przeciwnym razie (jeśli NIE jest większa 0)...
    print('Nie podałeś liczby większej niz 0') # ...wyświetl.



### Operator trójargumentowy (TERNARY OPERATOR) / Warunek w jednej linii.
# Znany również jako WYRAŻENIE WARUNKOWE, to sposób na zapisanie prostej instrukcji if-else w jednej, zwięzłej linii kodu.
# Służy do przypisywania wartości warunkowo.

# SKŁADNIA
# <wartość_jesli_true> if <warunek> else <wartość_jesli_false>

num11 = 11

# Taki kod można zapisać jak niżej:

if num11 % 2 == 0:
    wynik = 'Parzysty'
else:
    wynik = 'Nieparzysty'
print(wynik)

# lub w jednej linii:

wynik = 'Parzysty' if num11 % 2 == 0 else 'Nieparzysty'
print(wynik)


### ZADANIE – Zakupy
# Użytkownik podaje cenę produktu.
# Za pomocą TERNARY OPERATOR przypisz do zmiennej status:
# – "Drogi", jeśli cena > 100
# – "Tani", jeśli cena ≤ 100.

product_price = int(input('Podaj cenę produkty. '))
print('Tani') if product_price <= 100 else print('Drogi')



### Warunek z NON

var = None

if not var: # Można zapisać w taki sposób
    print('Var jest puste')

if var is None:
    print('Var jest puste')  # jednak bezpieczniej jest zapisać w taki sposób.
