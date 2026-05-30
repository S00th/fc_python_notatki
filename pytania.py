# ####### PYTANIA I WĄTPLIWOŚCI
#
### Przykład z materiałów z kursu – zapis ""
#
# tekst = "Przykładowy tekst."
# if tekst:
#     print("Ta linia zostanie wykonana")
# tekst = ""
# if tekst:
#     print("To polecenie zostanie pominięte")



# # ####### RÓŻNICA między .isdigit, a .isnumeric.
#
# word1, word2, word3, word4, word5, word6, word7 = '2026', 'python', '3.14', '314&', '²', '½', '三'
# print(word1.isdigit()) # True, bo składa się z cyfr
# print(word2.isdigit()) # False, bo składa się z liter alfabetu
# print(word3.isdigit()) # False, bo nie akceptuje .
# print(word4.isdigit()) # False, bo nie akceptuje znaków specjalnych
# print(word5.isdigit()) # True, bo rozpoznaje indeks górny ² i dolny ₂
# print(word6.isdigit()) # False, bo nie rozpoznaje ułamków zapisanych w formie ½ (Unicode)
# print(word7.isdigit()) # False, bo nie akceptuje liczb z innych systemów pisma np. 三 (japońskie 3).
#
# word1, word2, word3, word4, word5, word6, word7 = '2026', 'python', '3.14', '314&', '²', '½', '三'
# print(word1.isnumeric()) # True, bo składa się z cyfr
# print(word2.isnumeric()) # False, bo składa się z liter alfabetu
# print(word3.isnumeric()) # False, bo nie akceptuje .
# print(word4.isnumeric()) # False, bo nie akceptuje znaków specjalnych
# print(word5.isnumeric()) # True, bo rozpoznaje indeks górny ² i dolny ₂
# print(word6.isnumeric()) # True, bo rozpoznaje ułamki zapisane w formie ½ (Unicode)
# print(word7.isnumeric()) # True, bo rozpoznaje liczb z innych systemów pisma np. 三 (japońskie 3).



# ####### Czy tupla może myć KLUCZEM w SŁOWNIKU?
#
# list = ['Adam', 15, 15.5, True]
# tuple = ('Adam', 15, 15.5, True)
# set = {'Adam', 15, 15.5, True}
# dict = {'name': 'Ewa', 'age': 20 }
#
# print(list)
# print(type(list))
# print()
#
# print(tuple)
# print(type(tuple))
# print()
#
# print(set)
# print(type(set))
# print()
#
# print(dict)
# print(type(dict))
# print()
#
# dict2 = {('Adam', 15, 15.5, True): 'Ewa', 'age': 20 }
# print(dict2)
# print(type(dict2))



####### ĆWICZENIE z instrukcjami warunkowymi
# Przykład myślenia/kombinowania na ZDANIACH (pytanie-odpowiedź + zależności), a nie ZADANIACH matematycznych (pasjonat?).
# Zadania matematyczne powodują, że muszę się skupić/cofnąć w myśleniu 2 poziomy wcześniej –
# nie myślę nad rozwiązaniem problemu na zasadzie "jak to opisać kodem", tylko zanim do tego się zabiorę,
# tylko myślę "Na czym polegało, to działanie matematyczne" – a matematykę miałem w szkole średniej (skostniała wiedzy frustruje).
# Oczywiście nie chodzi o to, że mam zamiar ignorować działania matematyczne w programowaniu (raczej się nie da),
# po prostu, łatwiej mi zrozumieć PODSTAWY, kiedy operuje na ZDANIACH lub prostych działaniach matematycznych.
# Lubie WYZWANIA LOGICZNE (planszówki), ale zaawansowana matematyka nie.
# Niżej przykład. Miałem problem ze zrozumieniem instrukcji zagnieżdżonych. Kiedy pomyślałem w taki sposób jak niżej – "załapałem".

# name = input('Jak masz na imię? ')
#
# if name.lower() == 'szymon':
#     print(f'Cześć {name.capitalize()}! Miło znów cię widzieć.')
#     gotowy = input('Czy jesteś gotowy do pracy? ')
#     if gotowy.lower() == 'tak':
#         print('To świetnie. Zabierajmy się do pracy')
#     else:
#         chory = input('Czy czujesz się chory? ')
#         if chory.lower() == 'tak':
#             print('Poproś przełożonego o urlop i udaj się do lekarza!')
#         else:
#             print('Jakoś dasz radę! Zabierajmy się do pracy.')
# else:
#     print(f'Cześć {name.capitalize()}. Miło mi się poznać.')



### ĆWICZENIE – Przysiady
# Przykład, który pomógł zrozumieć pętle "while".

# squats = 0 # Zaczynam ćwiczenie. W tym momencie "zrobiłem" zero przysiadów,
#             # ale w czasie trwania programu WARTOŚĆ zmiennej squats zostanie zmodyfikowana.
#
# while squats <= 5: # Dopóki nie wykonam 5 przysiadów...
#     print(squats) # wyświetl, który przysiad właśnie zrobiłem...
#     squats += 1 # dodaj koleje przysiad i wróć pierwszego wiersza kodu (zaczynającego się od "while")



####### Czy było?

# OPERATORY IDETYCZNOŚCIOWE
# Określają, czy dwie zmienne przechowują ten sam obiekt. Mamy dwa operatory identycznościowe:
# is
# not is
#
# x = "ala ma kota"
# y = "ala nie ma kota"
# if x is not y:
#     print("Obiekty x i y to nie te same obiekty")
# x = y
# if x is y:
#     print("Obiekty x i y to  te same obiekty")
#
# # OPERATORY PRZYNALEŻNOŚCI
# # Sprawdzają, czy dany element zawiera się w podzbiorze wartości danego obiektu. Mamy dwa takie operatory:
# # in
# # not in
#
# x = "ala ma kota"
# if "ma" in x:
#     print("wyraz 'ma' występuje w ciągu'",x,"'")
# y = [2, 3, 4, 100]
# if 4 in y:
#     print("Liczba 4 występuje w zbiorze",y)
# else:
#     print("Liczba 4 nie występuje w zbiorze",y)



###

# Użytkownik wpisuje hasło.
# Program ma sprawdzić:
# – czy hasło ma minimum 8 znaków
# – czy pierwszy znak NIE jest cyfrą
# – czy w haśle znajduje się znak "!" lub "?"
# – czy hasło nie zaczyna się i nie kończy tą samą literą
#
# Niejednoznaczność.
#
# Użytkownik wpisuje hasło.
# Program ma sprawdzić czy spełnione są następujące warunki:
# - hasło ma się składać z minimum 8 znaków
# - hasło ma się zaczynać NIE-cyfrą
# - hasło ma zawierać znaki "!" i "?"
# - hasło NIE zaczyna się i kończyć tą samym literą

# Dany jest moduł string.
# Zbuduj funkcję do generowania haseł.
# Funnkcja powinna przyjmować następujące wartości
#     żądana długość hasła.
#     czy zawrzeć znaki specjalne jeśli True to zawszyj, jeśli False, to nie zawieraj
# Na końcu wymieszaj litery.
#
# Zbuduj program go generowania haseł oparty na podanym module string.
# Powinien on:
# - zapytać o długość hasła, które chce utworzyć
# - dać możliwość wyboru czy w skład hasła mają wejść znaki specjalne
# - na końcu ma wymieszać znaki/litery, z których składa się hasło