secret_number = 777
print(
    """
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")


number = int(input('Guess the number: '))

while number != secret_number:
    print("Haha! You're stuck in my loop")
    number = int(input('Guess another number: '))

print("Well done, mugglle! You are free now.")
