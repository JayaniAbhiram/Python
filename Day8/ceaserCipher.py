alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("type encrypt or decrypt of ur choce: ")

text = input("enter the text you wanna pass: ").lower()
shift = int(input("enter hoiw may char u wanna shift: "))


def encrypt(text,shift):
    for letter in text:
        position = alphabet.index(letter)
        newPosition = position+ shift
    


encrypt(text,shift)


