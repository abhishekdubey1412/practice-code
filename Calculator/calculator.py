from art import logo

# Addition
def addition(a,b):
    return a + b

# Subtraction
def subtraction(a,b):
    return a - b

# Multiplication
def multiplication(a,b):
    return a * b

# Division
def division(a,b):
    return a / b

Operations = {
    "+" : addition,
    "-" : subtraction,
    "*" : multiplication,
    "/" : division,
}

def calculator():
    print(logo)

    num1 = float(input("What's the first number? "))

    for symbol in Operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operations_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))
        calculator_function = Operations[operations_symbol]
        answer = calculator_function(num1, num2)

        print(f"{num1} {operations_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation. ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()
calculator()