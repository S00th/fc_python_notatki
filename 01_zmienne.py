####### ZMIENNE i TYPU DANYCH w Pythonie

# ZMIENNE (variables) można wyobrazić sobie jako pudełka, w których przechowywane sę różne informacje.
# Umożliwiają one zapisanie danych (np. LICZB lub TEKSTU), nadać im nazwę, a także wracać do nich podczas wykonywanego programu.
# Python jest językiem TYPOWANYM DYNAMICZNIE, co oznacza, że podczas przypisywania WARTOŚCI do ZMIENNEJ
# nie musimy deklarować TYPU DANYCH (Python sam zarządzi miejscem w pamięci). Pod jedną zmienną możemy podstawiać różne typy danych.
# Zrozumienie zmiennych to fundament, na którym zbudujesz całą swoją wiedzę o programowaniu.

### Kluczowe CECHY ZMIENNYCH w Pythonie

# Każda ZMIENNA musi mieć swoją unikalną NAZWĘ oraz przypisaną do niej WARTOŚĆ.
# WARTOŚĆ przypisujemy za pomocą OPERATORA PRZYPISANIA (znaku równości).
# NAZWA (name) zmiennej znajduje się zawsze po lewej stronie OPERATORA PRZYPISANIA (znaku równości).
# WARTOŚĆ (value) zmiennej znajduje się po prawej stronie OPERATORA PRZYPISANIA (znaku równości).
# Przykład: wiek = 40.
# Nazwa zmiennej MOŻE składać się z: DUŻYCH i małych liter alfabetu łacińskiego, cyfr, oraz znaku _
# UWAGA! WARTOŚĆ wpisana przez użytkownika sama w sobie PRZECHOWUJE WARTOŚĆ LOGICZNĄ.

# Nazwa ZMIENNEJ nie może:
# – zawierać SPACJI
# – zawierać znaków diakrytycznych: ą, ć, ę, ł, ń, ó, ś, ź, ż, np. polskich znaków – żółć
# – zawierać znaków specjalnych: !, @, #, $, %, ^, &, *, (, ), -, +, =, {, }, [, ], |, \, :, ;, ", ', <, >, ,, ., ?, /, np. !Aga$
# – zaczynać się od cyfry, np. 123_name
# – być słowem kluczowym Pythona, ani nazwą funkcji wbudowanej, np. print, if, class
#
# WIELKOŚĆ LITER (case sensitivity)
# Python odróżnia małe i wielkie litery. Oznacza to, że zmienne o nazwach Aga i aga będą traktowane jako zupełnie różne zmienne.
#
# DYNAMICZNE TYPOWANIE (dynamic typing)
# W przeciwieństwie do wielu innych języków, w Pythonie podczas przypisywania WARTOŚCI do ZMIENNEJ (zanim zostanie użyta)
# nie musisz deklarować TYPU DANYCH (mówić komputerowi, czy w pudełku jest LICZBA, czy TEKST).
# Python sam rozpozna TYPU DANYCH na podstawie tego, co przypiszesz do ZMIENNEJ.
#
# SŁOWA ZAREZERWOWANE (keywords)
# Istnieją pewne słowa, których nie możecie użyć jako NAZW ZMIENNYCH, ponieważ mają specjalne znaczenie dla języka Python – np. print, if, class.
#
# WIELOKROTNE UŻYCIE
# Raz zdefiniowaną ZMIENNĄ możesz wywoływać wielokrotnie, co pozwala uniknąć powtarzania tego samego kodu i ułatwia wprowadzanie zmian.



####### TYPY DANYCH W PYTHONIE:

# TYPY DANYCH określają rodzaj informacji, jakie są przechowywane w zmiennych.
# Od TYPU DANYCH zależy, jakie operacje można na nich wykonywać (np. LICZBY można dodawać, a TEKSTY łączyć)
# Typy danych możemy podzielić na PROSTE i ZŁOŻONE.

# Numeryczne (typ prosty):
#   – Integers (int): LICZBY CAŁKOWITE, np. 2 lub -2. Liczby całkowite mogą być dowolnie duże (lub małe) i mogą przyjmować wartości ujemne.
#   – Floats (float): LICZBY ZMIENNOPRZECINKOWE (ułamkowe), np. 2.5
#
# Teksty (typ prosty):
#   – Strings (str): TEKSTY, zawsze zapisywane w cudzysłowie, np. "Dwa" lub "2.5". Każda treść umieszczona w cudzysłowie jest traktowana jako tekst
#
# Wartości logiczne (typ prosty):
#   – Booleans (bool): WARTOŚCI LOGICZNE, czyli prawda (True) lub fałsz (False). Muszą zaczynać się wielką literą
#
# STRUKTURY DANYCH (typ złożony)
#   – Listy [list]
#   – Krotki (tuple)
#   – Zbiory {set}
#   – Słowniki [dict]
#
# NONTYPE
#   – None: Posiada swój własny, unikalny typ o nazwie "NoneType". Jest on oddzielony od LICZB, TEKSTÓW i WARTOŚCI LOGICZNYCH.

