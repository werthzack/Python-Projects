alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def cipher(text: str, shift: int, direction: str):
    ciphered_info = []
    for letter in text:
        if not letter.isalpha():
            ciphered_info.append(letter)
            continue
        upper = letter.isupper()
        letter = letter.lower()
        index = alphabet.index(letter)
        ciphered_letter = ""

        if direction == "decode":
            ciphered_letter = alphabet[(index + shift) % 26]
        else:
            ciphered_letter = alphabet[(index - shift) % 26]

        if upper:
            ciphered_letter = ciphered_letter.upper()

        ciphered_info.append(ciphered_letter)
    return ''.join(ciphered_info)


active = True

while active == True:
    instruction = input("Type 'encode' to encrpyt and 'decode' to decrypt: ")
    text = input("Input Your Message: \n")
    shift = int(input("Input the shift number: "))

    print(cipher(text, shift, instruction))

    active = True if input("Continue? Y/N: \n") == "Y" else False
