def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Division by zero!"
    except TypeError:
        return "Error: Invalid operand types!"

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    result = divide(num1, num2)
    print("Result:", result)
except ValueError:
    print("Error: Invalid input. Please enter valid numbers.")
