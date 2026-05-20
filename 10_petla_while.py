####### PĘTLA WHILE
# Dobrą praktyką programistyczną jest pisanie kodu w taki sposób, aby wymagał od nas jak najmniejszego nakładu pracy.
# Bez potrzeb powtarzania go czy zmieniania w wielu miejscach.

# Do tej pory kod wykonywał się linijka po linijce (wyjątkiem były instrukcje warunkowe).
# Pętle wykonują pewien fragment kodu określoną ilość czasu/razy.
# Pętla WHILE ("dokupi") wykonuje się do momentu, kiedy zostanie spełniony podany przez nas wcześniej warunek.
# Pętla WHILE zakończy się, kiedy warunek z WYRAŻENIA PRAWDZIWEGO stanie się wyrażeniem FAŁSZYWYM.
# ITERACJA to proces wielokrotnego wykonywania tego samego bloku. Realizujemy ją w pętli "while" i "for".
# Operator przypisania złożonego (Augmented assignment) += jest stosowany zamiast zapisu: licznik = licznik +1.

# STRUKTURA
# while <warunek, który jest prawdziwy (trzeba spełnić)>:
#     <blok kodu, który się powtarza>
# print('Wyjście z pętli while.'))


wiek = int(input('Podaj mi swój wiek: '))
uprawniony_do_emerytury = False

while wiek < 65: # Pętla WHILE zakończy się, kiedy warunek z WYRAŻENIA PRAWDZIWEGO stanie się wyrażeniem FAŁSZYWYM.
    print(f'Niestety nie możesz przejść na emeryturę. Twój wiek to {wiek}.')
    wiek += 1
uprawniony_do_emerytury = True # Jeżeli ktoś wpisze liczbę większą niż 65, to pętla nawet nie zostanie uruchomiona.
print('Jesteś już na emeryturze.')



#### INFINITE LOOP / Niekończącej się pętla.
# Nie wpisaliśmy nigdzie kodu, który zmniejszałby cenę domu.

cena_domu = float(input('Podaj cenę domu: '))
budzet = 1_000_000

while budzet < cena_domu:
    print('Niestety nie stać cię na dom. Poczekaj, aż właściciel opuści cenę')



#### PĘTLA while True – Inny przykład, niekończącej się pętli.

# while True:
#     print('Nie przerwiesz mnie.') # Ta pętla nigdy się nie skończy.

###

wiek = int(input('Podaj mi swój wiek: '))
while True:
    wiek += 1
    if wiek < 65:
        print(f'Nie możesz jeszcze przejść na emeryturę. Masz {wiek} lat.')
    else:
        print("Jesteś już w wieku emerytalnym")
        break # <- to słowo kluczowe w instrukcji kluczowej, które przerywa pętlę.



### Instrukcja BREAK
# Z instrukcji "break" będziemy korzystali podczas przeszukiwania struktur danych.
# Kiedy podczas przeszukiwania znajdziemy to, czego szukaliśmy, nie ma sensu kontynuować poszukiwań i w takim momencie wchodzi instrukcja break.

wiek = int(input('Podaj mi swój wiek: '))
while True:
    wiek += 1
    if wiek == 18:
        print('Nie martw się o emeryturę. Korzystaj z życia!') # Niżej przykład co zrobić, aby nie wyświetlać tej linii razem z "Nie możesz..."
    if wiek < 65:
        print(f'Nie możesz jeszcze przejść na emeryturę. Masz {wiek} lat.').
    else:
        print("Jesteś już w wieku emerytalnym")
        break # <- to słowo kluczowe w instrukcji kluczowej, które przerywa pętlę.



### Instrukcja CONTINUE

wiek = int(input('Podaj mi swój wiek: '))
while True:
    wiek += 1
    if wiek == 18:
        print('Nie martw się o emeryturę. Korzystaj z życia!')
        continue # <- instrukcja, która powoduje przejście do kolejnej iteracji (wraca do: wiek += 1)
    if wiek < 65:
        print(f'Nie możesz jeszcze przejść na emeryturę. Masz {wiek} lat.')
    else:
        print("Jesteś już w wieku emerytalnym")
        break



### Instrukcja PASS – Instrukcja pustej linii
# Stasujemy ją, kiedy wiemy, że będziemy coś robić, ale jeszcze nie wiemy co konkretnie.

wiek = int(input('Podaj mi swój wiek: '))
while True:
    wiek += 1
    if wiek == 25: # Jeśli wpisalibyśmy tutaj if pod if, to wyświetli się błąd.
        pass # Zastosowanie instrukcji gwarantuje nam, że nie wyświetli się błąd spowodowany błędną składnią.
    if wiek == 18:
        print('Nie martw się o emeryturę. Korzystaj z życia!')
        continue # <- instrukcja, która powoduje przejście do kolejnej iteracji (wraca do: wiek += 1)
    if wiek < 65:
        print(f'Nie możesz jeszcze przejść na emeryturę. Masz {wiek} lat.')
    else:
        print("Jesteś już w wieku emerytalnym")
        break