""" if the year number isn't divisible by four, it's a common year;
otherwise, if the year number isn't divisible by 100, it's a leap year;
otherwise, if the year number isn't divisible by 400, it's a common year;
otherwise, it's a leap year. """

year = int(input("Enter a year: "))

if year < 1582:
    print(f" {year} isn't in the Gregorian Calendar ,"
          "please put a year after 1581")
    exit()

if year % 4 != 0:
    print(f'{year} it is a common year')

elif year % 100 != 0:
    print(f'{year} it is a leap year')

elif year % 400 != 0:
    print(f'{year} it is a common year')

else:
    print(f'{year} it is a leap year')
