from random import choice

bohater = {
    'Gandalf': 'Człowiek',
    'Boromir': 'Człowiek',
    'Legolas': 'Elf',
    'Frodo': 'Niziołek',
    'Gimli': 'Krasnolud'
}

losowy_bohater = choice(list(bohater.keys()))

pytanie = input(f'Jakies rasy był {losowy_bohater}? ')

if bohater[losowy_bohater] == pytanie:
    print(f'Bardzo dobrze. {losowy_bohater} to {bohater[losowy_bohater]}')
else:
    print(f'Niestety nie. {losowy_bohater} to {bohater[losowy_bohater]}')

# przygotuj słownik językowy
