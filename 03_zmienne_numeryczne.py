####### TYPY ZMIENNYCH

# ZMIENNE (Variables) można wyobrazić sobie jako pudełka, w których przechowywane sę różne informacje.
# Umożliwiają one zapisanie danych (np. liczb lub tekstu), nadać im nazwę i wracać do nich w dalszej części wykonywanego programu.
# Zrozumienie zmiennych to fundament, na którym zbudujesz całą swoją wiedzę o programowaniu.

# NAZWA zmiennej znajduje się zawsze po lewej stronie znaku równości,
# po prawej stronie znajduje się jej WARTOŚĆ.
# nazwa = wartość
# Nazwa zmiennej MOŻE składać się z dużych i małych liter alfabetu łacińskiego, cyfr, oraz znaku "_".
# UWAGA! WARTOŚĆ wpisana przez użytkownika sama w sobie PRZECHOWUJE WARTOŚĆ LOGICZNĄ.

# Nazwa ZMIENNEJ nie może:
    # zawierać SPACJI
    # zawierać znaków diakrytycznych: ą, ć, ę, ł, ń, ó, ś, ź, ż, np. polskich znaków – żółć
    # zawierać znaków specjalnych: !, @, #, $, %, ^, &, *, (, ), -, +, =, {, }, [, ], |, \, :, ;, ", ', <, >, ,, ., ?, /, np. !Aga$
    # zaczynać się od cyfry, np. 123_name
    # być słowem kluczowym Pythona, ani nazwą funkcji wbudowanej, np. print, if, class

####### TYPY DANYCH W PYTHONIE:

#   Numeryczne:
#       – Integers (int): Liczba całkowita, np. 2 lub -2. Liczby całkowite mogą być dowolnie duże (lub małe) i mogą przyjmować wartości ujemne
#       – Floats (float): Liczba zmiennoprzecinkowa (z ułamkiem), np. 2.5
#   Teksty
#       – Strings (str): Teksty, zawsze zapisywane w cudzysłowie, np. "Dwa" lub "2.5". Każda treść umieszczona w cudzysłowie jest traktowana jako tekst
#   Wartości logiczne
#       – Booleans (bool): Wartości logiczne, czyli prawda (True) lub fałsz (False). Muszą zaczynać się wielką literą


# Konwencje zapisu ZMIENNYCH i KLAS
tax_rate = 0.23 # ZMIENNE i FUNKCJE nazywaj w konwencji snake_case
taxRate = 0.23 # KLASY nazywaj w konwencji CamelCase, a konkretnie lowerCamelCase
TaxRate = 0.23 # KLASY nazywaj w konwencji CamelCase, a konkretnie UpperCamelCase (nazywanej też Pascal Case)
TAX_RATE = 0.23 # STAŁE nazywaj w tej konwencja (chociaż dla Pythona STAŁE i ZMIENNE to, to samo)

EARTH_RADIUS_KM = 6397 # STAŁA, specjalny przypadek zmiennej
PI = 3.14 # STAŁA, specjalny przypadek zmiennej

####### Zmienne NUMERYCZNE

### INTEGERS (int): Liczby całkowite, np. 2 lub -2. Liczby całkowite mogą być dowolnie duże (lub małe) i mogą przyjmować wartości ujemne.

x = 3 # Można przypisać kilka liczby do kilku ZMIENNYCH jak tutaj – czyli każda zmienna w oddzielnej linii
y = 30
z = 10
# lub
x, y, z = 3, 30, 10 # Można przypisać kilka liczb do kilku ZMIENNYCH jednej linii.

print(type(2)) # Sprawdź typ danych
print(type(-2))
print(type(2.5))
print(type('dwa'))
print(type(True))

# Podpowiadanie typów – TYPE ANNOTATION / TYPE HINTING
height: int = 180 # Python sam rozpoznaje typy danych, ale można mu je podpowiedzieć
height = 'napis'

# SEPARATOR WIZUALNY – Separator tysięczny
miliard_v1 = 1_000_000_000 # Aby ułatwić sobie odczyt wielkich liczb, możemy użyć separatora wizualnego _
print(miliard_v1)
miliard_v2 = 1000000000 # PYTHON nie widzi różnicy między zapisem wyżej o tym obok.
print(miliard_v2)

# Separator dziesiętny – W PYTHONIE separatorem dziesiętnym jest KROPKA
data = 1.0 # float # Prawidłowy zapis liczby 1.0 w PYTHONIE (z KROPKĄ).
data2 = 1,0 # tuple # Zapis z PRZECINKIEM spowoduje, że PYTHON nie zauważy liczby 1.0, a ZBIÓR DANYCH (tuple) składającą się z 1 i 0.
print(type(data), type(data2))

# Zaokrąglenie (Rounding)
pi = 3.14159265359
print(round(pi, 3))
print(round(pi))

# integer vs rounding
num = 3.89
print(int(num)) # INTEGER nie zaokrągla, po prostu ucina wartość po przecinku.
print(round(num)) # round zaokrągla w górę lub w dół (do bliższej wartości) UWAGA! num = 3.50 to 4.

# f-string rounding
print(f'PI 2 decimal places {pi:.4f}') # Nowoczesnym i bardzo czytelnym sposobem łączenia tekstów ze zmiennymi,
# która automatycznie dba o konwersję typów i jest uważany za styl Pythonic.
