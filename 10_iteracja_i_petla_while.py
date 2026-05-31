####### ITERACJA, PĘTLE i PĘTLA WHILE
#
# Dobrą praktyką programistyczną jest pisanie kodu w taki sposób, aby wymagał od nas jak najmniejszego nakładu pracy.
# Kod należy pisać w taki sposób, aby nie było potrzeby powtarzania go lub zmieniania w wielu miejscach.
# Do tej pory kod wykonywał się linijka po linijce (wyjątkiem były instrukcje warunkowe) w przypadku pętli będzie to wyglądało inaczej.

# ITERACJA (powtórzenie) to proces wielokrotnego wykonywania określonej operacji lub bloku kodu...
# w celu wykonania zadania do momentu spełnienia określonego warunku lub zadaną liczbę razy.
# Proces ten jest niezbędny do automatyzacji powtarzalnych czynności.
#
# W języku Python ITERACJĘ realizuje się głównie za pomocą PĘTLI.
# Inaczej mówiąc, PĘTLE wykonują pewien fragment kodu OKREŚLONĄ ILOŚĆ CZASU/RAZY.
# Pozwalają uniknąć ręcznego przepisywania tych samych instrukcji.
#
# PĘTLA "while"– wykonuje się, DOPÓKI twierdzenie JEST PRAWDZIWE (może NIESKOŃCZONĄ ilość razy).
# POWTARZA blok kodu tak długo, JAK DŁUGO DANY WARUNEK logiczny JEST PRAWDZIWY (True).
# Inaczej mówiąc, pętla WHILE zakończy się, kiedy WARUNEK Z WYRAŻENIA PRAWDZIWEGO stanie się wyrażeniem FAŁSZYWYM.
# Jest idealna w sytuacjach, gdy liczba powtórzeń nie jest znana przed uruchomieniem pętli.
#
# PĘTLA "for" – wykonuje się SKOŃCZONA/OKREŚLONĄ ilość razy.
# Używana, GDY WIEMY, ILE RAZY dana OPERACJA MA ZOSTAĆ POWTÓRZONA lub gdy chcemy PRZEJŚĆ przez WSZYSTKIE ELEMENTY w ZBIORZE danych (w LIŚCIE lub SŁOWNIKU).
# W programowaniu często stosuje się ją w konstrukcji "for in range", która pozwala na precyzyjne określenie liczby powtórzeń

# DODATKOWE KOMENDY (komendy sterujące) – służą do precyzyjnego sterowania procesem ITERACJI:
# Występują wyłącznie wewnątrz pętli (FOR oraz WHILE).
#
# BREAK
# Pozwala na natychmiastowe PRZERWANIE PĘTLI i wyjście z niej, nawet jeśli warunek końcowy nie został jeszcze osiągnięty.
# Interpreter przechodzi do wykonywania instrukcji znajdujących się bezpośrednio po bloku pętli.
# Przydatny, gdy np. SZUKAMY KONKRETNEGO ELEMENTU na LIŚCIE i po jego znalezieniu NIE CHCEMY już sprawdzać pozostałych danych.
#
# CONTINUE
# Powoduje POMINIĘCIE reszty INSTRUKCJI w bieżącej ITERACJI (powtórzeniu) i natychmiastowe przejście do kolejnej ITERACJI PĘTLI.
# W przeciwieństwie do BREAK, PĘTLA nie jest przerywana na stałe
# Program "przeskakuje" do kolejnego ELEMENTU lub SPRAWDZENIA WARUNKU PĘTLI, ignorując instrukcje, które znajdują się poniżej słowa CONTINUE w danej pętli.
# Przydatna, gdy chcemy ZIGNOROWAĆ (odfiltrować) pewne konkretne przypadki, ale KONTYNUOWAĆ przetwarzanie pozostałych danych.


### OPERATOR PRZYPISANIA ZŁOŻONEGO (augmented assignment)
# Jest to sposób na skrócenie zapisu operacji matematycznej i jednoczesnego PRZYPISANIE WYNIKU operacji do zmiennej.
# Zamiast wykonywać czynności w dwóch oddzielnych krokach (najpierw obliczenie, potem przypisanie nowej wartości do zmiennej)...
# możesz to zrobić za pomocą jednego symbolu, co czyni kod bardziej zwięzłym i czytelnym
# OPERATOR += (dodawanie i przypisanie) jest stosowany zamiast zapisu: licznik = licznik +1.

# OPERATORY PRZYPISANIA ZŁOŻONEGO
# Operatory te łączą standardowy OPERATOR PRZYPISANIA (=) z OPERATORAMI ARYTMETYCZNYMI (+ - * / % **).
# += Dodawanie i przypisanie: += b -> a = a + b
# -= Odejmowanie i przypisanie: a -= b -> a = a - b
# *= Mnożenie i przypisanie: a *= b -> a = a * b
# /= Dzielenie i przypisanie: a /= b -> a = a / b
# %= Reszta z dzielenia i przypisanie: a %= b -> a = a % b
# **= Potęgowanie i przypisanie: a **= b -> a = a ** b


# STRUKTURA pętli WHILE
# while <warunek, który jest prawdziwy (wykonywany, dopóki jest prawdziwy)>:
#     <blok kodu, który się powtarza>
# print('Wyjście z pętli while.'))


# STRUKTURA pętli WHILE (inny zapis)
#
# while <warunek1>:
#     <kod znajdujący się po wcięciu, jest kodem, który jest wykonywany, dopóki warunek jest prawdziwy>
#     if <warunek2>: break # wyjście z pętli (pominięcie reszty)
#     if <warunek3>: continue # przejście do góry pętli powrót do warunek1)
# else:
#     {kod wykonywany, jeśli pętli nie zakończyło break}



### ĆWICZENIE – Przysiady
# Planujesz zrobić 5 przysiadów.
# Stwórz pętle, która będzie działałą do momentu, aż zrobisz 5 przysiadów.


squats = 0 # Zaczynam ćwiczenie. W tym momencie zrobiłem ZERO przysiadów,
            # ale w czasie trwania programu WARTOŚĆ zmiennej "squats" zostanie zmodyfikowana.

while squats <= 5: # Dopóki nie wykonam 5 przysiadów...
    print(squats) # wyświetl, który przysiad właśnie zrobiłem...
    squats += 1 # dodaj koleje przysiad i wróć do pierwszego wiersza kodu (zaczynającego się od "while")


### ĆWICZENIE – Miejsca w busie.

bus_chairs = 0
while bus_chairs <= 20: # Jeżeli liczba wolnych miejsc (bus_chairs) jest mniejsze niż 20, to wejdź do busa.
    passenger = int(input('Ile osób weszło do busa? ')) # Pobierz informację, ile osób weszło do busa tym razem?
    bus_chairs += passenger # Powiększ zmienną "bus_chairs" o liczbę osób, które weszły (passenger)
    print(f'W busie siedzi już {bus_chairs} osób.') # Wyświetl, ile osób znajduje się aktualnie w busie.


### ĆWICZENIE – Droga do sklepu
# Użytkownik znajduje się w drodze do sklepu.
# Zapytaj, czy już dodarł do sklepu.
# Jeśli nie – niech jedzie dalej.
# Jeśli tak – poinformuj go, że dotarł do sklepu.

store = False
while not store: # Dopóki nie dotrzesz do sklepu...
    question = input('Czy dotarłeś do sklepu? [T/N] ') # Zadawaj pytanie, czy dotarłeś do sklepu.
    if question.upper() == 'T': # Jeżeli WARUNEK zostanie spełniony (potwierdziłeś, że dotarłeś do sklepu)
        print('Dotarłeś do sklepu') # Wyświetl komunikat...
        store = True # i zmień warunek wejściowy na prawdziwy.
    else:
        print('Jedź dalej.') # W przeciwnym przypadku "Jedź dalej" i wróci do początku pętli.



### ĆWICZENIE
#

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



### ĆWICZENIE
#
# Kalkulator, który sumuje koszt zakupów.
# Poproś użytkownika o nazwę: produkty, niech poda liczbę sztuk oraz cenę za sztukę.
# Po wprowadzeniu danych zapytaj użytkownika, czy chce zakończyć lub wprowadzić kolejny produkt.

# Zmienna, która odpowiada za łączną wartość produktów, musi się znajdować na samej górze programu – przed pętlą "while".
# Gdyby znajdowała się wewnątrz pętli, za każdym uruchomieniem pętli tworzylibyśmy nową zmienną z przypisaną wartością 0.

suma = 0 # Sumę tą będziemy zwiększać podczas działania pętli.

while True:
    produkt = input('Podaj nazwę produktu: ')
    ilosc = int(input('Podal liczbę sztuk: '))
    cena = float(input('Podaj cenę za kilogram: '))

    wartosc = ilosc * cena
    suma += wartosc # Znaczy to tyle, co: suma = wartosc + suma

    print(f'Produkt: {produkt}. Koszt: {wartosc} zł.')

    odpowiedz = input('Wprowadź kolejny produkt [T] lub zakończ [N]: ')
    if odpowiedz.upper() == 'N':
        break
print(f'Łączny koszta zakupów wynosi {suma} zł.') # Wyświetl sumę już poza pętlą
