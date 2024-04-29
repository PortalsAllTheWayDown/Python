suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']

for suit in suits:
    abbrev = suit[0].upper()
    print(f'{abbrev} = {suit}')

for i in range(2,11,2):
    print(i)

for i in range(3):
    for j in range(3):
        print(f'i={i}, j={j}')
    print('-' * 10)