
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
#bug fixed
shift%=26

def encrypter(text, shift):
    position = 0
    cipher_text = ""
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
        new_position = position+shift
        cipher_text += alphabet[new_position]
    print(f"The encoded text is {cipher_text}")


def decrypter(text, shift):
    position = 0
    cipher_text = ""
    shift*=-1
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
        new_position = position+shift
        cipher_text += alphabet[new_position]
    print(f"The decoded text is {cipher_text}")


if direction == "encode":
    encrypter(text, shift)

elif direction == "decode":
    decrypter(text, shift)
