import enc

while True:
    ask = input('Welcome to Zkrail\'s Encryptor.\n\nWould you like to, [encrypt] or [decrypt]?\n\n')
    if ask == 'encrypt':
        enc.data.askencryption()
    elif ask == 'decrypt':
        enc.data.askdecryption()
    else:
        print("Hey! That\'s not an option!")
