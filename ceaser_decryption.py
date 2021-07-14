def decrypt(text, key):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Decrypt Upper Case Text or Characters

        if (char.isupper()):
            result += chr((ord(char) + key - 65) % 26 + 65)

        # Decrypt Lower Case Text or Characters

        else:
            result += chr((ord(char) + key - 97) % 26 + 97)

    return result


text = input("Enter Message to Decrypt: ")
key = int(input("Enter the decryption key: "))
key %= 26
print("Text: " + text)
print("Key: " + str(key))
print("Decrypted Message: " + decrypt(text, 26 - key))
