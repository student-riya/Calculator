from datetime import datetime

# Input date as a string
date_string = input("Enter a date in the format DD/MM/YYYY: ")

try:
    # Split the input string into day, month, and year
    day, month, year = map(int, date_string.split('/'))
    
    # Try to construct a date object (will raise ValueError if invalid)
    date_object = datetime(year, month, day)
    
    print("The entered date is valid.")
    print(f"Day: {day}, Month: {month}, Year: {year}")

except ValueError:
    print("Invalid date entered. Please check the day, month, or year format.")
