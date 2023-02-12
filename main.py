import enc

ask = input('Welcome to Zkrail\'s Encryptor.\n\nWould you like to, [encrypt] or [decrypt]?\n\n')

while True:
    if ask == 'encrypt':
        enc.data.askencryption()
    elif ask == 'decrypt':
        enc.data.askdecryption()
    else:
        print("Hey! That\'s not an option!")