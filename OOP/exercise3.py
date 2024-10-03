def division(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y

try:
    result = division(7, 14)
    print(f"The result is {result}")
except ZeroDivisionError as e:
    print(e)
