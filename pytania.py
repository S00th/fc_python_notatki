# ####### PYTANIA itp.
#
### ĆWICZENIE – Cykl życia projektu AI
# 1. Zdefiniuj problem.
# Czy udało ci się zdefiniować problem? [T/N]
# 2. Znajdź dane
# Czy zgromadziłeś wszystkie niezbędne dane? [T/N]
# 3. Spróbuj bez AI
# Czy udało ci się rozwiązać problem bez pomocy AI? [T/N]
# 4. Utwórz siatkę bezpieczeństwa
# Czy utworzyłeś siatkę bezpieczeństwa? [T/N]
# 5. Wytrenuj model.
# Czy wytrenowałeś model? [T/N]
# 6. Zdobądź feedback
# Czy zdobyłeś feedback? [T/N]
# 7. Monitoruj.
# Czy zbudowane rozwiązanie AI działa? [T/N]
# Czy chcesz zacząć nowy cykl?



### ĆWICZENIE wprowadzające do pracy domowej
#

def powitanie(name: str, age: int, is_married: str):
    if is_married.upper() == 'T':
        return f'Witaj, {name}, masz {age} lat. Jesteś zamężna/żonaty.'
        # Mam problem z zapamiętaniem żeby dodać "return", że nie wywołuje WYNIKU DZIAŁANIA FUNKCJI tylko samą FUNKCJĘ.
    else:
        return f'Witaj, {name}, masz {age} lat. Nie jesteś zamężna/żonaty.'

name = input('Jak masz na imię? ')
age = input('Ile masz lat? ')
is_married = input('Czy jesteś zamężna/żonaty? [T/N] ')

print(powitanie(name, age, is_married))



### ĆWICZENIE – Praca domowa – Generator HASEŁ
#
# Dany jest moduł "strip".
# Zbuduj funkcję do generowania haseł.
# Funkcja powinna przyjmować następujące argumenty:
# – Żądana długość hasłą (funkcja umożliwia podanie żądanej długości hasłą).
# – Czy zawrzeć znaki specjalne, jeśli True to zawrzyj, jeśli False to nie zawieraj.
# – No końcu wymieszaj litery.
# Otypuj argumenty, wartości zwracane. Dokonaj niezbędnej walidacji wejścia.

import string # Definiujemy zestawy znaków globalnie (raz na początku)
import random

def pass_gen(pass_len: int, spec_char: str):
    if not isinstance(pass_len, int) or not isinstance(spec_char, str): # Mam problem z działającą WALIDACJĄ
        raise TypeError('Podałeś nieprawidłowe dane wejściowe.')
    if spec_char.upper() == 'T':
        pass_range = pass_all_val_list
    else:
        pass_range = pass_not_all_val_list
    combined_char_in_password = random.choices(pass_range, k=pass_len) # Losuje powtarzające się znaki (można BEZ: random.sample)
    return ''.join(combined_char_in_password) # Połączenie w jedne string

pass_all_val_list = list(string.ascii_letters + string.digits + string.punctuation) # Tworzę LISTĘ dla dwóch wariantów
pass_not_all_val_list = list(string.ascii_letters + string.digits)
# print(pass_all_val)
# print(pass_not_all_val)

pass_len = int(input('Z ilu znaków ma się składać hasło? '))
spec_char = input('Czy chcesz, aby w haśle znalazły się znaki specjalne? [T/N] ')

new_pass = pass_gen(pass_len, spec_char)
print(f'Twoje nowe hasło to: {new_pass}')
