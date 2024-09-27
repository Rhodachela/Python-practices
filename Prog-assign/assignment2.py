def calculate_tax(income):
    first_bracket_income = 10000
    second_bracket_income = 15000
    third_bracket_income = 25000

    first_tax = 0
    second_tax = 0.1
    third_tax = 0.15

    if income <= first_bracket_income:
        tax = first_bracket_income * first_tax
    elif income <= first_bracket_income + second_bracket_income:
        tax = (first_bracket_income * first_tax) + ((income - first_bracket_income) * second_tax)
    else:
        tax = ((first_bracket_income * first_tax) + (second_bracket_income * second_tax)) + ((income - (first_bracket_income + second_bracket_income)) * third_tax)
    return tax

income = float(input("Enter your monthly income: "))
tax = calculate_tax(income)
print(f"The income payable tax is {tax} Ksh")


#(b)
def calculation_grades():
    score = int(input("Enter your score: "))
    if score in range(0, 40):
        grade = "F"
    elif score in range(40, 50):
        grade = "E"
    elif score in range(50, 60):
        grade = "D"
    elif score in range(60, 70):
        grade = "C"
    elif score in range(70, 80):
        grade = "B"
    elif score in range(80, 101):
        grade = "A"
    else:
        print("Invalid score! Please try again.")
        return None
    return grade


final_grade = calculation_grades()
if final_grade:
    print(f"Your grade is {final_grade}")
