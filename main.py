def encrypt_message(message, key):
    encrypted = ''
    for letter in message:
        if ord(letter) > 96 and ord(letter) < 123:
            pre_ord = ord(letter) + key
            if pre_ord > 122:
                pre_ord -= 26
            if pre_ord < 97:
                pre_ord += 26
            encrypted += chr(pre_ord)
        else:
            encrypted += letter
    return encrypted


def decrypt_message(message, key):
    decrypted = ''
    for letter in message:
        if ord(letter) > 96 and ord(letter) < 123:
            pre_ord = ord(letter) - key
            if pre_ord > 122:
                pre_ord -= 26
            if pre_ord < 97:
                pre_ord += 26
            decrypted += chr(pre_ord)
        else:
            decrypted += letter
    return decrypted


def hacking(message):
    the_list = []
    for letter in message:
        if ord(letter) > 96 and ord(letter) < 123:
             if the_list == []:
                 the_list.append(ord(letter))
             elif len(the_list) == 1 and (the_list[0] - ord(letter) == 12 or the_list[0] - ord(letter) == -14):
                 the_list.append(ord(letter))
             elif len(the_list) == 2 and (the_list[0] - ord(letter) == 15 or the_list[0] - ord(letter) == -11):
                 the_list.append(ord(letter))
             else:
                 the_list = []
        else:
            if len(the_list) == 3:
                key = the_list[0] - 116
                if key <= 0: key+= 26
                return key
            the_list = []
    return 0

d = open('book.txt', 'r')
text = d.read()
key = 8

print(text)

encrypted = encrypt_message(text, key)
print(encrypted)

newkey = hacking(encrypted)
print(newkey, newkey == key)

decrypted = decrypt_message(encrypted, newkey)
print(decrypted)

d.close()
