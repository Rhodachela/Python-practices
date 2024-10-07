class ValueTooHighError(Exception):
    pass
def check_value(number):
    if number > 100:
        raise ValueTooHighError(f"Error: The value {number} is too high. Try again!")
    else:
        print(f"The value {number} is within the required range")
    
try:
    number = int(input("Enter number: "))
    check_value(number)
except ValueTooHighError as e:
    print(e)
except ValueError:
    print("Invalid input. Enter a proper integer.")