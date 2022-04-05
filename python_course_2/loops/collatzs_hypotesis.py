number = int(input('Insert the number: '))

c0 = number
counting_tries = 0


while c0 != 1:
    if c0 % 2 == 0:
        c0 = int(c0 / 2)
        print(c0)
    else:
        c0 = int(3 * c0 + 1)
        print(c0)
    counting_tries += 1

print(f'took {counting_tries} steps until the end of the loop')
