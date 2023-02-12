import os
from cryptography.fernet import Fernet as f
from datetime import datetime
import base64 as b64

class data:

    def encryption(data,key):
        time = datetime.now()
        while True:                 # Ran into a problem where it had to be 32 digits, so I used this little code here to fix it.
            if len(key) == 32:      # Sadly it breaks if you have a key more than 32 digits.
                break               # I will work on that later. Probably.
            elif len(key) != 32:
                key = f'{key}s'
        skey = bytes(key,encoding='utf-8')
        enkey = b64.urlsafe_b64encode(skey)
        akey = f(enkey)
        cmp = akey.encrypt(data.encode())
        cla = str(cmp)
        al = cla.replace('b\'', '')
        end = al.replace('\'', '')
        try:
            os.chdir('encryption')
        except:
            os.mkdir('encryption')
            os.chdir('encryption')
        file = open(f'{time} - OUTPUT',"w")
        file.write(f'OUTPUT AT {time}\n\n{end}')
        print("Job Completed")
    
    def askencryption():
        idata = input('What item would you like to encrypt?\n')
        ikey = input('\nYour passkey?\n[WARNING] Your passkey cannot be longer than 32 digits. [WARNING]\n')

        data.encryption(idata,ikey)

    def askdecryption():
        addata = input('What item would you like to decrypt?')
        adkey = input('What is the key?')

        data.decryption(addata,adkey)

    def decryption(data,key):
        time = datetime.now()
        while True:
            if len(key) == 32:
                break
            elif len(key) != 32:
                key = f'{key}s'
        skey = bytes(key,encoding='utf-8')
        ddata = bytes(data,encoding='utf-8')
        enkey = b64.urlsafe_b64encode(skey)
        akey = f(enkey)
        dnp = akey.decrypt(ddata).decode()
        try:
            os.chdir('decryption')
        except:
            os.mkdir('decryption')
            os.chdir('decryption')
        file = open(f'{time} - OUTPUT',"w")
        file.write(f'OUTPUT AT {time}\n\n{dnp}')
        print("Job Completed")
