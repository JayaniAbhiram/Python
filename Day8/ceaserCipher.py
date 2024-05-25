alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from ceaserCipherArt import logo
print(logo)

def ceaser():
    direction = input("type encode or decode of ur choce: ")

    text = input("enter the text you wanna pass: ").lower()
    shift = int(input("enter hoiw may char u wanna shift: "))
    shift = shift % 26
    if direction == "encode":
        cipherText = ""
        for letter in text:
            if letter not in alphabet:
                letter = letter
                cipherText = cipherText + letter
            else:
                position = alphabet.index(letter)
                newPosition = position+ shift
                newLetter = alphabet[newPosition]
                cipherText = cipherText + newLetter
        print("the encoded text is :" + cipherText)
    elif(direction == "decode"):
        cipherText = ""
        for letter in text:
            if letter not in alphabet:
                letter = letter
                cipherText = cipherText + letter
            else:
                position = alphabet.index(letter)
                newPosition = position - shift
                newLetter = alphabet[newPosition]
                cipherText = cipherText + newLetter
        print("the decoded text is: " + cipherText)
    else:
        print("choose either encode or decode")


ceaser()

end = False

while not end:     
    # ceaser()
    nextStep = input("choose continue to continue and bye to end: ")
    if nextStep == "bye":
        end = True
    else:
        ceaser()

    
    
print("game over")

