####### TYPY ZMIENNYCH

# Nazwa ZMIENNEJ nie może:
    # zawierać znaków specjalnych: !, @, #, $, %, ^, &, *, (, ), -, +, =, {, }, [, ], |, \, :, ;, ", ', <, >, ,, ., ?, /, np. !Aga$
    # zawierać znaków diakrytycznych: ą, ć, ę, ł, ń, ó, ś, ź, ż, np. polskich znaków – żółć
    # zaczynać się od cyfry, np. 123_name
    # być słowem kluczowym Pythona, ani nazwą funkcji wbudowanej, np. print, if, class
        # print = 12
        # print('Aga')

# Konwencje zapisu ZMIENNYCH i KLAS
tax_rate = 0.23 # ZMIENNE i FUNKCJE nazywaj w konwencji snake_case
taxRate = 0.23 # KLASY nazywaj w konwencji CamelCase, a konkretnie lowerCamelCase
TaxRate = 0.23 # KLASY nazywaj w konwencji CamelCase, a konkretnie UpperCamelCase (nazywanej też Pascal Case)
TAX_RATE = 0.23 # STAŁE nazywaj w tej konwencja (chociaż dla Pythona stałe i zmienne to, to samo)

EARTH_RADIUS_KM = 6397 # STAŁA, specjalny przypadek zmiennej
PI = 3.14 # STAŁA, specjalny przypadek zmiennej

####### Zmienne numeryczne

### Integers (int): Liczby całkowite, np. 2 lub -2. Liczby całkowite mogą być dowolnie duże (lub małe) i mogą przyjmować wartości ujemne.

x = 3 # Można przypisać kilka liczby do kilku zmiennych jak tutaj, czyli każda zmienna w oddzielnej linii.
y = 30
z = 10
# lub
x, y, z = 3, 30, 10 # Można też przypisać kilka liczb do kilku zmiennych jednej linii.

print(type(2)) # Sprawdź pyt danych
print(type(-2)) # Sprawdź pyt danych
print(type(2.5)) # Sprawdź pyt danych
print(type('dwa')) # Sprawdź pyt danych
print(type(True)) # Sprawdź pyt danych

# Podpowiadanie typów – TYPE ANNOTATION / TYPE HINTING
height: int = 180
height = 'napis'

# Separator wizualny – Separator tysięczny
miliard_v1 = 1_000_000_000
miliard_v2 = 1000000000

print(miliard_v1)
print(miliard_v2)

# Separator dziesiętny
data = 1.0 # float
data2 = 1,0 # tuple
print(type(data), type(data2))

# Zaokrąglenie (Rounding)
pi = 3.14159265359
print(round(pi, 3))
print(round(pi))

# integer vs rounding
num = 3.89
print(int(num)) # int nie zaokrągla, po prostu ucina wartość po przecinku
print(round(num)) # round zaokrągla w górę lub w dół

# f-string rounding
print(f"PI 2 decimal places {pi:.4f}") # nowoczesna metoda konkatenacji tekstu i też może być wykorzystywana do zaokrąglania tekstu