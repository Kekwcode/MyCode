
num1 = float(input("Enter number: "))
op = (input("Enter Operator: "))
num2 = float(input("Enter number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Invalid")