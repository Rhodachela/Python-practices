#(a)
print("DAYS OF THE WEEK")
day = int(input("Enter the day of the week: "))
if day == 1:
    print("Hope you had a nice weekend.")
elif day == 2:
    print("Settle down for serious work")
elif day == 3:
    print("Its mid week")
elif day == 4:
    print("Ladies night")
elif day == 5:
    print("The weekend is back")
elif day == 6:
    print("Rest day")
elif day == 7:
    print("Plan for the week ahead")
else:
    print("Invalid input. Try again")

#(b)
CELSIUS_TO_FAHRENHEIT = 9/5 
FAHRENHEIT_TO_CELSIUS = 5/9

def convert_to_fahrenheit():
    global  CELSIUS_TO_FAHRENHEIT
    fahrenheit = (CELSIUS_TO_FAHRENHEIT * temperature) + 32
    return fahrenheit

def convert_to_celsius():
    global FAHRENHEIT_TO_CELSIUS
    celsius = (temperature - 32) * FAHRENHEIT_TO_CELSIUS
    return celsius

temperature = float(input("Enter the temperature to convert: "))
unit = input("Is this temperature in celsius or fahrenheit (C/F)?: ").upper()
if unit == "C":
    fahrenheit = convert_to_fahrenheit()
    print(f"The result is {fahrenheit}°F")
elif unit == "F":
    celsius = convert_to_celsius()
    print(f"The result is {celsius}°C")
else:
    print("Invalid input!")