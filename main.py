#importing functions for required operations
import calculator

#Prompting user for input for calculator
print("Welcome to simple calculator.")
print("I will add/subtract/multiple/divide any two numbers you provide.")
first_input = input("Enter in first number: ")
second_input = input("Enter in second number: ")
operation = input("Would you like to add/subtract/multiply/divide: ")

#Converting input to float
first_number = float(first_input)
second_number = float(second_input)

#code to execute operation based on input
if operation == "add":
    calculator.add(first_number, second_number)
elif operation == "subtract":
    calculator.subtract(first_number, second_number)
elif operation == "multiply":
    calculator.multiply(first_number, second_number)
elif operation == "divide":
    calculator.divide(first_number, second_number)
else:
    print("Sorry, I do not understand your request.")
