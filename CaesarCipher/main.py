import art, json

with open('data.json', 'r') as file:
    alphabet = json.load(file)

print(art.logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("\nType your message:\n").lower()
shift = int(input("\nType the shift number:\n"))


def input_user(d):
    if d == 'encode':
        encrypt(t=text, s=shift)

    if d == 'decode':
        decrypt(t=text, s=shift)


def encrypt(t, s):
    text_encrypt = ''
    for letter in t:
        solution_index = (alphabet.index(letter))+s 
        text_encrypt += alphabet[solution_index]
    
    print(f'\nThe encoded text is "{text_encrypt}".\n')


def decrypt(t, s):
    text_decrypt = ''
    for letter in t:
        solution_index = (alphabet.index(letter))-s
        text_decrypt += alphabet[solution_index]
    
    print(f'\nThe decoded text is "{text_decrypt}"\n')
    

input_user(d=direction)

def caesar(t,s,d):
    new_text = ''
    if d == 'decode':
        s *= -1
    
    for letter in t:
        new_index = (alphabet.index(letter))+s
        new_text += alphabet[new_index]

    print(f"Here's the {direction}d result: '{new_text}'.\n")

caesar(t=text, s=shift, d=direction)