# Project: Simple Console Calculator
# Author: [VAISHNAVI TIWARI]
#Regn No : 25BAI10696
# Date:22 November 2025
# Description: A basic calculator supporting addition, subtraction, multiplication, and division
# using function calls and a main loop.

# --- Function Definitions for Operations ---

def add(n1, n2):
    """Returns the sum of two numbers."""
    return n1 + n2

def subtract(n1, n2):
    """Returns the difference of two numbers."""
    return n1 - n2

def multiply(n1, n2):
    """Returns the product of two numbers."""
    return n1 * n2

def divide(n1, n2):
    """Returns the quotient of two numbers. Handles division by zero error."""
    if n2 == 0:
        # Custom error message for invalid operation
        return "Error! Cannot divide by zero."
    return n1 / n2

# --- Main Program Logic ---

def calculator():
    """
    Runs the main calculator loop, handling user input and operation execution.
    """
    print("---------------------------------")
    print("  SIMPLE CONSOLE CALCULATOR")
    print("---------------------------------")
    print("Select operation:")
    print("1. Add      (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide   (/)")
    print("5. Exit")
    print("---------------------------------")

    while True:
        # Get user's choice of operation
        choice = input("Enter choice (1/2/3/4/5): ")

        # Check if choice is valid
        if choice in ('1', '2', '3', '4'):
            try:
                # Get number inputs from the user, converted to floating point for flexibility
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid Input. Please enter a number.")
                continue # Go back to the start of the loop

            result = None

            # Execute the selected operation
            if choice == '1':
                result = add(num1, num2)
                operation = "+"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = "-"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = "*"
            elif choice == '4':
                result = divide(num1, num2)
                operation = "/"

            # Display the result to the user
            print(f"\nResult: {num1} {operation} {num2} = {result}\n")

        elif choice == '5':
            print("Thank you for using the Simple Calculator. Goodbye!")
            break # Exit the loop and end the program

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Entry point of the script
if __name__ == "__main__":
    calculator()