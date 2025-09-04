def get_year():
    return int(input("Please enter your year: "))

def check_leap(year):
    if year % 100 == 0 and year % 400 != 0:
        print("This is not a leap year.")
    if year % 4 == 0:
        print("This is a leap year.")
    else:
        print("This is not a leap year.")

year = get_year()
check_leap(year)
