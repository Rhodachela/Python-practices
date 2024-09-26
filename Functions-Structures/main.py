from arithmetic_operations import perform_operation

def main():  
    while True:
        print("Arithmetic operations")
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Enter a valid integer")
            break
            
        operation = str(input("Enter the operation (add, subtract, multiply, divide): ")).strip().lower()  
       
        if operation == "quit":
            print("Exiting the program. Goodbye!")
            break
        
        result = perform_operation(num1, num2, operation)
        print(f"The result is {result}")

if __name__ == "__main__":
    main()
