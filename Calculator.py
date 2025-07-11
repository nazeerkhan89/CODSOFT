"""
Simple Calculator Program
Author: [Your Name]
Date: [Current Date]
Version: 1.0
"""

def add(num1, num2):
    """Addition operation"""
    return num1 + num2

def subtract(num1, num2):
    """Subtraction operation"""
    return num1 - num2

def multiply(num1, num2):
    """Multiplication operation"""
    return num1 * num2

def divide(num1, num2):
    """Division operation with zero division check"""
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "Error! Division by zero."

def get_number_input(prompt):
    """Get valid number input from user"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_operation_input():
    """Get valid operation choice from user"""
    while True:
        operation = input("Choose operation (+, -, *, /): ").strip()
        if operation in ['+', '-', '*', '/']:
            return operation
        print("Invalid operation. Please choose from +, -, *, /")

def display_result(num1, num2, operation, result):
    """Display the calculation result"""
    print(f"\nCalculation Result: {num1} {operation} {num2} = {result}")

def main():
    """Main calculator function"""
    print("SIMPLE CALCULATOR")
    print("-----------------")
    
    # Get user inputs
    num1 = get_number_input("Enter first number: ")
    num2 = get_number_input("Enter second number: ")
    operation = get_operation_input()
    
    # Perform calculation
    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    elif operation == '/':
        result = divide(num1, num2)
    
    # Display result
    display_result(num1, num2, operation, result)

if __name__ == "__main__":
    while True:
        main()
        continue_calc = input("\nDo you want to perform another calculation? (y/n): ").lower()
        if continue_calc != 'y':
            print("Thank you for using the calculator. Goodbye!")
            break
