def is_year_leap(year):
    if year < 1582:
        print("Not within the Gregorian calendar period")
        return False
    else:
        if year % 4 != 0:
            return False
        elif year % 100 != 0:
            return True
        elif year % 400 != 0:
            return False
        else:
            return True

def days_in_month(year, month):
    if year < 1582 or month < 1 or month > 12:
        return None

    month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month == 2 and is_year_leap(year):
        return 29
    return month_lengths[month - 1]

def day_of_year(year, month, day):
    if year < 1582 or month < 1 or month > 12 or day < 1:
        return None

    days_in_current_month = days_in_month(year, month)
    if day > days_in_current_month:
        return None

    days = 0
    for m in range(1, month):
        days += days_in_month(year, m)

    days += day
    return days

# Testing the function
print(day_of_year(2000, 12, 31))  # Expected output: 366 (2000 is a leap year)
print(day_of_year(2020, 3, 1))    # Expected output: 61 (2020 is a leap year)
print(day_of_year(2019, 3, 1))    # Expected output: 60 (2019 is not a leap year)
print(day_of_year(1581, 3, 1))    # Expected output: None (year not within Gregorian calendar period)
print(day_of_year(2020, 2, 30))   # Expected output: None (February 30 is invalid)
print(day_of_year(2020, 4, 31))   # Expected output: None (April 31 is invalid)
