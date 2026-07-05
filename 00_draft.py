import csv

with open("data/csv_files/osoby.csv", encoding="utf-8") as plik_wejsciowy:
    reader = csv.DictReader(plik_wejsciowy)

    pelnoletni = [osoba for osoba in reader if int(osoba["wiek"]) >= 18] # List comprehension automatycznie tworzy listę.

with open("data/csv_files/pełnoletni.csv", mode="w", encoding="utf-8", newline="") as plik_wyjsciowy:
    writer = csv.DictWriter(plik_wyjsciowy, fieldnames=["imie", "nazwisko", "wiek"])
    writer.writeheader()
    writer.writerows(pelnoletni)