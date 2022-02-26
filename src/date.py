def is_year_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if month in  [1, 3, 5, 7, 8, 10, 12]:
        return 31
    if month in  [4, 6, 9, 11]:
        return 30
    if month == 2:
        if is_year_leap(year):
            return 29
        else:
            return 28
    return None

def day_of_year(year, month, day):
    if year <= 0:
        return None
    if month < 1 or month > 12:
        return None
    if day < 1 or day > days_in_month(year, month):
        return None
    return "%d/%d/%d"%(day, month, year)

print(day_of_year(2020, 2, 29))