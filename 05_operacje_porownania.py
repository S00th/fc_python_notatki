####### OPERATOR PRZYPISANIA oraz OPERATORY LOGICZNE (operacje porównania)
#
# Kluczowe cechy ZMIENNYCH w Pythonie
# – Każda ZMIENNA musi mieć swoją unikalną NAZWĘ oraz przypisaną do niej WARTOŚĆ.
#   Nazwa (Name) i wartość (Value)
#   Wartość przypisujemy za pomocą znaku równości (operator przypisania), na przykład: wiek = 25.
#
# – WIELKOŚĆ LITER (Case sensitivity): Python odróżnia małe i wielkie litery.
#   Oznacza to, że zmienne o nazwach Zmienna, zmienna oraz ZMIENNA będą traktowane jako trzy zupełnie różne pudełka.
#
# – DYNAMICZNE TYPOWANIE (Dynamic typing)
#   W przeciwieństwie do wielu innych języków, w Pythonie podczas przypisywania wartości do zmiennej (przed użyciem zmiennej)
#   nie musisz deklarować typu danych (mówić komputerowi, czy w pudełku jest liczba, czy tekst).
#   Python sam rozpozna typ danych na podstawie tego, co przypiszesz do ZMIENNEJ.
#
# – SŁOWA ZAREZERWOWANE (Keywords)
#   Istnieją pewne słowa, których nie możecie użyć jako nazw zmiennych, ponieważ mają one specjalne znaczenie dla języka Python – np. print, if, class.
#
#  – WIELOKROTNE UŻYCIE
#   Raz zdefiniowaną zmienną możesz wywoływać wielokrotnie, co pozwala uniknąć powtarzania tego samego kodu i ułatwia wprowadzanie zmian.



# OPERATORY PORÓNANIA służą do zestawiania ze sobą dwóch wartości w celu określenia relacji między nimi.
# Zawsze zwracają wartość logiczną bool (Boolean), czyli zmienną logiczną True (prawda) lub False (fałsz).

a = 10
b = 5

# Operatory porównania:

print(a == b) # Zwraca True, jeśli obie wartości są IDENTYCZNE
print(a != b) # Zwraca True, jeśli obie wartości są RÓŻNE
# Użycie: == != między różnymi typami danych zwróci False, ponieważ LICZBA nie może być identyczna z TEKSTEM.

print(a > b) # Zwraca True, jeśli lewa wartość jest WIĘKSZA od prawej
print(a >= b) # Zwraca True, gdy lewa wartość jest WIĘKSZA lub równa prawej
print(a < b) # Zwraca True, jeśli lewa wartość jest MNIEJSZA od prawej
print(a <= b) # Zwraca True, gdy lewa wartość jest MNIEJSZA lub równa prawej
# Użycie: > < >= <= między różnymi typami zmiennych wywoła TypeError

print('adam' == 'Adam') # False – ponieważ wielkość liter ma znaczenie