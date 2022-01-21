alfavit =  " 1234567890абвгдеёжзийклмнопрстуфхцчшщъыьэюя.,;:!?'«»—()"
message = ""
f = open('book.txt', 'r')
key = 7

for i in f.read():
    if i.lower() in alfavit:
        message += i.lower()

def encrypt_message(message, key):
    encrypted = ''
    for i in message:
        n = alfavit.find(i) + key
        if n >= len(alfavit):
            n -= len(alfavit)
        if n < 0:
            n += len(alfavit)
        encrypted += alfavit[n]
    return encrypted


def decrypt_message(message, key):
    decrypted = ''
    for i in message:
        n = alfavit.find(i) - key
        if n >= len(alfavit):
            n -= len(alfavit)
        if n < 0:
            n += len(alfavit)
        decrypted += alfavit[n]
    return decrypted

def hacking(message):
    counter = dict.fromkeys(alfavit, 0)
    for i in message:
        if i in counter:
            counter[i] += 1
    maxcount = 0
    maxletter = '0'

    for letter in counter:
        if counter[letter] > maxcount:
            maxcount = counter[letter]
            maxletter = letter
    newkey = alfavit.find(maxletter)
    return newkey
print(message.lower())
encrypted = encrypt_message(message.lower(), key)
print(encrypted)

newkey = hacking(encrypted)
print(newkey)

decrypted = decrypt_message(encrypted, newkey)
print(decrypted)