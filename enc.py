import os
from cryptography.fernet import Fernet as f
from datetime import datetime
import base64 as b64

class data:

    def encryption(data,key):
        time = datetime.now()
        key = key.replace(" ","")
        while True:                 # Ran into a problem where it had to be 32 digits, so I used this little code here to fix it.
            if len(key) == 32:      # Used to break if you have a key more than 32 digits.
                break               # I fixed it.
            elif len(key) < 32:
                key = f'{key}s'
            elif len(key) > 32:
                key = key[:-1]
            else:
                break
        al = ((str(f(b64.urlsafe_b64encode(bytes(key,encoding='utf-8'))).encrypt(data.encode()))[1:])[1:])[:-1]
        try:
            os.chdir('encryption')
        except:
            os.mkdir('encryption')
            os.chdir('encryption')
        file = open(f'{time} - OUTPUT',"w").write(f'OUTPUT AT {time}\n\n{al}')
        print(f'\nJob Completed\nOutput:\n{al}')
    
    def askencryption():
        idata = input('\nWhat item would you like to encrypt?\n')
        ikey = input('\nYour passkey?\n')
        try:
            data.encryption(idata,ikey)
        except:
            print("How did you mess that up? Well, you did. Try again. Something went wrong.")

    def askdecryption():
        addata = input('\nWhat item would you like to decrypt?\n')
        adkey = input('\nWhat is the key?\n')
        try:
            data.decryption(addata,adkey)
        except:
            print("Item or Key Invalid.")

    def decryption(data,key):
        time = datetime.now()
        key = key.replace(" ","")
        while True:                
            if len(key) == 32:      
                break               
            elif len(key) < 32:
                key = f'{key}s'
            elif len(key) > 32:
                key = key[:-1]
            else:
                break
        dnp = f(b64.urlsafe_b64encode(bytes(key,encoding='utf-8'))).decrypt(bytes(data,encoding='utf-8')).decode()
        try:
            os.chdir('decryption')
        except:
            os.mkdir('decryption')
            os.chdir('decryption')
        file = open(f'{time} - OUTPUT',"w").write(f'OUTPUT AT {time}\n\n{dnp}')
        print(f'\nJob Completed\nOutput:\n{dnp}')
