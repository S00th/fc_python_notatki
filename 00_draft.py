####### DRAFT
#

suma_mb_filmow = 0
ilosc_slotow = 1 # Utworze przynajmniej 1 slot więc zaczynam od 1, a nie od 0.
max_wielkosc_slotu = 10_000
aktualna_wielkosc_slotu = 0
najlzejszy_slot = 1
wielkosc_najlzejszego_slotu = 10_000
najciezszy_slot = 0

ilosc_filmow = int(input('Ile filmów chcesz dodać na serwer? '))

for ilosc_filmow in range(ilosc_filmow): # Zapis: range(ilosc_filmow), jest tożsamy z: range(0, ilosc_filmow)
    rozmiar_filmu = float(input('Podaj rozmiar filmu: '))
    if 100 > rozmiar_filmu > 3_000: # Jeżeli film będzie mniejszy niż 100 MB lub większy niż 3000 MB...
        break # Przerwij
    suma_mb_filmow += rozmiar_filmu
    if rozmiar_filmu + aktualna_wielkosc_slotu <= max_wielkosc_slotu: # Jeżeli spełniony jest ten warunek...
        aktualna_wielkosc_slotu += rozmiar_filmu # To dodaje tą wartość.
    else: # A jeżeli nie...
        if aktualna_wielkosc_slotu < wielkosc_najlzejszego_slotu: # Na rozmiar slotu patrzę w momencie, kiedy skończę ładować do niego dane.
            najlzejszy_slot = ilosc_slotow # Ilość slotów mówi nam też, na którym slocie aktualnie jesteśmy (można ją jakby przypisać do drugiej rzeczy).
            wielkosc_najlzejszego_slotu = aktualna_wielkosc_slotu # Po to, żebyśmy mieli slot, który ma 8_000, a nie 10_000.
        aktualna_wielkosc_slotu = ilosc_filmow # Zamykam slot...
        ilosc_slotow += 1 # i dodaje nowy film do poprzedniego.
print()
print(f'Całkowity rozmiar filmów: {suma_mb_filmow} MB.')
print(f'Ilość wykorzystanych slotów: {ilosc_slotow}.')
print(f'Pusta przestrzeń dyskowa: {ilosc_slotow * max_wielkosc_slotu - suma_mb_filmow} MB')
print(f'Najlżejszy slot, to slot {najlzejszy_slot} z dostępną pojemnością {wielkosc_najlzejszego_slotu}.')

# Do zrobienia jest jeszcze jedno sprawdzenie, które już jest w tym kodzie:

# if 100 > rozmiar_filmu > 3_000:  # Jeżeli film będzie mniejszy niż 100 MB lub większy niż 3000 MB...
#     break  # Przerwij
# suma_mb_filmow += rozmiar_filmu
# if rozmiar_filmu + aktualna_wielkosc_slotu <= max_wielkosc_slotu:  # Jeżeli spełniony jest ten warunek...
#     aktualna_wielkosc_slotu += rozmiar_filmu  # To dodaje tą wartość.