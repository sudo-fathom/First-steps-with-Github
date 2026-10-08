import time
operator = input("Enter an operator: (+, -, /, *)")
time.sleep(1)

Num1 = float(input("Enter the first number: "))
time.sleep(1)

Num2 = float(input("Enter the second number: "))
time.sleep(1)

if operator == "+":
    print(f"The sum of the {Num1} and {Num2} is {Num1 + Num2}")
elif operator == "-":
    print(f"The difference of the {Num1} and {Num2} is {Num1 - Num2}")
elif operator == "/":
    print(f"The quotient of the {Num1} and {Num2} is {Num1 / Num2}")
elif operator == "*":
    print (f"The product of the {Num1} and {Num2} is {Num1 * Num2}")
else:
    print("Invalid operator")
