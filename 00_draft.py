from datetime import datetime, date

teraz = datetime.now()
print(teraz) # Wyświetli datę i dokłądną godzinę: 2026-06-16 17:38:05.465284
print(f'Godzina: {teraz.hour} / Minuta: {teraz.minute} / Sekunda: {teraz.second}') # Godzina: 17 / Minuta: 45 / Sekunda: 21

dzisiaj = date.today()
print(dzisiaj) # Wyświetli datę: 2026-06-16
print(type(dzisiaj)) # <class 'datetime.date'>
print(date.today().year) # Wyświetli: 2026
print(f'Rok: {dzisiaj.year} / Miesiąc: {dzisiaj.month} / Dzień: {dzisiaj.day}') # Rok: 2026 / Miesiąc: 6 / Dzień: 16


### Formatowanie DATY na własny użytek

date_string = dzisiaj.strftime('%d.%m.%Y') # Wyświetli: 16.06.2026. Formatuje i ZAMIENIA na STRING.
# Gdzie: d – dzień, m – miesiąc, Y – rok.
print(date_string)
print(type(date_string)) # <class 'str'>

# Zamiana TEKSTU na STRING

text = '09-06-2026'
to_datetime = datetime.strptime(text, '%d-%m-%Y')
print(to_datetime) # Wyświetli: 2026-06-16 00:00:00
print(type(to_datetime)) # Wyświetli: <class 'datetime.datetime'>


# Operacje arytmetyczne na czasie

from datetime import timedelta

print(dzisiaj + timedelta(days=1)) # Wyświetli: 2026-06-17 – jutrzejszy dzień
