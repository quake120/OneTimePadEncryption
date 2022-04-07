alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890,.?"
keyFile = open('newkey.txt', 'r')
key = keyFile.read()

def generateKeyFromNumbers():
    randNumbersFile = open('numbers.txt', 'r')
    randNumbers = randNumbersFile.read()
    newKeyFile = open('newkey.txt', 'w')
    numbers = randNumbers.split('\n')
    newKeyString = ""

    for i in range(len(numbers)):
        newKeyString += alphabet[int(numbers[i])]

    newKeyFile.write(newKeyString)


def encryptMessage(message):

    if (len(message) > len(key)):
        print("Not enough key data to process message of length " +
              str(len(message)))
        quit()

    encrypted = ""
    for i in range(len(message)):
        message_letter = alphabet.find(message[i].upper(), 0, len(alphabet))
        key_letter = alphabet.find(key[i], 0, len(alphabet))

        cipher_letter = message_letter + key_letter

        if (cipher_letter >= len(alphabet)):
            cipher_letter -= len(alphabet)

        encrypted += alphabet[cipher_letter]

    return encrypted


def unencrypt(encryptedString):
    decrypted = ""

    for i in range(len(encryptedString)):
        encrypted_letter = alphabet.find(encryptedString[i].upper(), 0,
                                         len(alphabet))
        key_letter = alphabet.find(key[i], 0, len(alphabet))

        cipher_letter = encrypted_letter - key_letter

        if (cipher_letter < 0):
            cipher_letter += len(alphabet)

        decrypted += alphabet[cipher_letter]

    return decrypted


def menu():
    menuResponse = input("1) Encrypt 2) Decrypt\nChoose an option: ")

    if (menuResponse == '1'):
        msg = input("Type message: ")
        encryptedMsg = encryptMessage(msg)
        print(encryptedMsg)
        menu()

    if (menuResponse == '2'):
        msg = input("Paste encrypted string: ")
        decrypted = unencrypt(msg)
        print(decrypted)
        menu()


menu()
#encryptMessage("this is a test the quick brown fox jumped over the lazy dog")
#unencrypt("33162PZGZ3E20871YVK4ZZW7.F1?X.EGYFDTY67F 57BT05AVJ2NF416V8W")
