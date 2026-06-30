import csv

with open('data/osoby.csv', encoding='utf-8') as infile:
    # reader = csv.DictReader(infile,)
    # print(list(reader))

    adults = []
    for osoba in reader:
        if int(osoba['wiek']) >= 18:
            print(osoba)
            adults.append(osoba)
        print(adults)

with open('data/adults.csv', mode='w', encoding='utf-8', newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['imie', 'nazwisko', 'wiek'])
    writer.writeheader()
    writer.writerows(adults)

# Zapis w jednej linijce

    adults = [osoba for osoba in reader if int(osoba['wiek']) >= 18]

with open('data/adults.csv', mode='w', encoding='utf-8', newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['imie', 'nazwisko', 'wiek'])
    writer.writeheader()
    writer.writerows(adults)
