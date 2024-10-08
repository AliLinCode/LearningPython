def is_year_leap(year):
    if year < 1582:
        print("Not within the Gregorian calendar period")
    else:
        if year%4 != 0:
            print("Common year")
            return False
        elif year%100 != 0:
            print("Leap year")
            return True
        elif year%400 != 0:
            print("Common year")
            return False
        else:
            print("Leap year")
            return True
def days_in_month(year, month):
    if year < 1582 or month < 1 or month > 12:
        return None

    month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


    if month == 2 and is_year_leap(year):
        return 29
    return month_lengths[month - 1]
#
    # Write your new code here.
    #

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")




