####### PĘTLA WHILE
# Dobrą praktyką programistyczną jest pisanie kodu w taki sposób, aby wymagał od nas jak najmniejszego nakładu pracy.
# Bez potrzeb powtarzania go czy zmieniania w wielu miejscach.

# Do tej pory kod wykonywał się linijka po linijce (wyjątkiem były instrukcje warunkowe).
# Pętle wykonują pewien fragment kodu określoną ilość czasu/razy.
# Pętla WHILE ("dokupi") wykonuje się do momentu, kiedy zostanie spełniony podany przez nas wcześniej warunek.
# Pętla WHILE zakończy się, kiedy warunek z WYRAŻENIA PRAWDZIWEGO stanie się wyrażeniem FAŁSZYWYM.
# UWAGA! Upewnij się, że kod wewnątrz while może zmienić warunek. Tak, by program nie wykonywał się w nieskończoność!
#
# ITERACJA to proces wielokrotnego wykonywania tego samego bloku. Realizujemy ją w pętli "while" i "for".
# Operator przypisania złożonego (Augmented assignment) += jest stosowany zamiast zapisu: licznik = licznik +1.



# STRUKTURA
# while <warunek, który jest prawdziwy (wykonywany, dopóki jest prawdziwy)>:
#     <blok kodu, który się powtarza>
# print('Wyjście z pętli while.'))


# STRUKTURA pętli while (inny zapis)
#
# while <warunek1>:
#     <kod, który jest wykonywany, dopóki warunek jest prawdziwy>
#     if <warunek2>: break # wyjście z pętli (pominięcie reszty)
#     if <warunek3>: continue # przejście do góry pętli powrót do warunek1)
# else:
#     {kod wykonywany, jeśli pętli nie zakończyło break}



wiek = int(input('Podaj mi swój wiek: '))
uprawniony_do_emerytury = False

while wiek < 65: # Pętla WHILE zakończy się, kiedy warunek z WYRAŻENIA PRAWDZIWEGO stanie się wyrażeniem FAŁSZYWYM.
    print(f'Niestety nie możesz przejść na emeryturę. Twój wiek to {wiek}.')
    wiek += 1
uprawniony_do_emerytury = True # Jeżeli ktoś wpisze liczbę większą niż 65, to pętla nawet nie zostanie uruchomiona.
print('Jesteś już na emeryturze.')



#### INFINITE LOOP / Niekończąca się pętla.
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
# Czasami może zaistnieć potrzeba wyjścia z wewnątrz pętli, zanim całość bloku zostanie wykonane. Służy do tego instrukcja break.
# Kiedy podczas przeszukiwania znajdziemy to, czego szukaliśmy, nie ma sensu kontynuować poszukiwań i w takim momencie wchodzi instrukcja break.
# Z instrukcji "break" będziemy korzystali podczas przeszukiwania struktur danych.

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
# Jeśli chcesz pominąć część kodu i w bloku (ale tylko w obecnym przebiegu), to możemy użyć zagnieżdżonego warunku if.

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