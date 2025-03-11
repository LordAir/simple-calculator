# Function
def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operation."

# Main 
def main():
    # input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Operation
    operation = input("Enter the operation (+, -, *, /): ")
    
    # Calculation
    result = calculate(num1, num2, operation)
    
    print(f"{num1} {operation} {num2} = {result}")

# Run
if __name__ == "__main__":
    main()
