text = input('Wpisz dowolny tekst: ')
center = len(text) // 2
modulo = len(text) % 2
correct_text = True

if text[0] != '@':
    print('Tekst MUSI zaczynać się od @.')
    correct_text = False
if text[-1].isalpha():
    print('Tekst MUSI kończyć się liczbą.')
    correct_text = False
if text[center] != 'x':
    print('Środkowym znakiem tekstu MUSI być X.')
    correct_text = False
if text[modulo] != 'x':
    print('Środkowym znakiem tekstu MUSI być X.')
    correct_text = False
if correct_text:
    print('Wiadomość zaakceptowana.')
