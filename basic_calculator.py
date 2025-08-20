def add(x,y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Math Error"
    return x / y

print("====Simple Calculator====")
print("Operations\n'1. Addition(+)'\n'2. Subtraction(-)'\n'3. Multiplication(*)'\n'4. Division(/)'")


operation = input("Please enter the symbol of the operation you want to perform(+, -, *, /).")
a = float(input("Enter the first number.\n"))
b = float(input("Enter the second number.\n"))


if operation == '+':
    result = add(a, b)
elif operation == '-':
    result = subtract(a, b)
elif operation == '*':
    result = multiply(a, b)
elif operation == '/':
    result = divide(a, b)
else:
    result = "Invalid Operator"


msg = f"The result of your {operation} is: {result}"
print(msg)