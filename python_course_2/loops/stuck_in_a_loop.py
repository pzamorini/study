print("""
Welcome to your new cage.
You won't be free unless you gave us the right
awnser.
Good luck.

""")

word = input('Insert here your guess: ')

while word != 'chupacabra':
    print("Haha, you're stuck in my loop!")
    word = input("Try another guess: ")
    if word == 'chupacabra':
        break

print("Ok. You're rigth. Get out of here.")
