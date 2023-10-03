
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while True:
    choice = input('Do you want to(e)ncrypt or (d)ecrypt?').lower()
    if choice.startswith('e'):
        mode ='encrypt'
        break
    elif choice.startswith('d'):
        mode = 'decrypt'


while True:
    maxKey = len(SYMBOLS) - 1
    print('Please enter the key (0 to {}) to use.'.format(maxKey))
    response = input('>').upper()
    if not response.isdecimal():
        continue

    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

print('Enter the message to {}.'.format(mode))
message = input('> ')

message = message.upper()

translated = ''

for symbol in message:
    if symbol in SYMBOLS:
        num = SYMBOLS.find(symbol)
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt' :
            num = num - key

        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)


        translated = translated + SYMBOLS[num]

    else:
         translated = translated + symbol

print(translated)



