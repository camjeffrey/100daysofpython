def calculator(num1, operator, num2):
    result = eval(f"{num1} {operator} {num2}")
    return result

num1 = input("Enter first number: ")
operator = input("+\n-\n*\n/\nType operator: ")
num2 = input("Enter second number: ")

initial_result = calculator(num1, operator, num2)
new_result = 0

print(f"{num1} {operator} {num2} = {initial_result}")

while True:
    mode = input("Press 'y' to continue calculating with previous result, 'n' to begin new calculation, or 'q' to quit: ")
    if mode not in ['y', 'n', 'q']:
        print("Invalid selection.")
    elif mode == 'y':
        operator = input("+\n-\n*\n/\nType operator: ")
        num2 = input("Enter second number: ")
        new_result = calculator(initial_result, operator, num2)
        print(f"{initial_result} {operator} {num2} = {new_result}")
        initial_result = new_result
    elif mode == 'n':
        num1 = input("Enter first number: ")
        operator = input("+\n-\n*\n/\nType operator: ")
        num2 = input("Enter second number: ")
        initial_result = calculator(num1, operator, num2)
        print(f"{num1} {operator} {num2} = {initial_result}")
    elif mode == 'q':
        break