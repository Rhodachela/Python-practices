#(a)
def details(name, city, age):
    print(f"My name is {name}. I come from {city}. I am {age} years old.")
    return
details("Rhoda", "L.A", 23)

#(b)
for i in range(0, 20):
    if i %2 != 0:
        print(i)

#(c)
print("Enter the four numbers")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
num4 = int(input("Enter the fourth number: "))

numbers = [num1, num2, num3, num4]
max_number = max(numbers)
min_number = min(numbers)

print(f"The maximum number is {max_number}")
print(f"The minimum number is {min_number}")

#(d)
def exponent(base, exp):
    result = 1
    for _ in range(exp):
        result *= base
    return result
print(exponent(2, 3))

#(e)
def calculation(x, y):
    result = (x + y) * (x - y)
    return result
result = calculation(50, 40)
print(f"The result is {result}")
