from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"The current date and time is {formatted_current_date}")

display_current_datetime()

def calculate_future_date():
    current_date = datetime.now()
    future_date = current_date + (timedelta(days))
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"The future date is {formatted_future_date}")

while True:
    days = int(input("Enter the number of days: "))
    if days == -1 or days == 0:
        print("Exiting the program. Bye!!!!")
        break
    else:
        calculate_future_date()
        break
        