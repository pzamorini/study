def is_year_leap(year):
    if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
        return True
    else:
        return False


def DaysInMonth(year, month):
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31

    elif month == 2:
        if is_year_leap(year):
            return 29
        else:
            return 28
    elif month in {4, 6, 8, 9, 11}:
        return 30
    else:
        return None


test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = DaysInMonth(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
