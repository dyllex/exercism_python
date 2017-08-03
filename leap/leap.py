def is_leap_year(year):

    # Year is leap year if it is divisible by 4 but not 100 unless the year
    # is divisible by 400
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
