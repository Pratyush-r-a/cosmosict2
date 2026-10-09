num1 = float(input("Enter first number: "))
symbol = input("enter operation:")
num2 = float(input("enter second number: "))

if symbol == "+":
    result = num1 + num2
    print("Result:", result)               

elif symbol == "-":
    result = num1 - num2
    print("Result:", result)

elif symbol == "*":
    result = num1 * num2
    print("Result:", result)

elif symbol == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("Invalid symbol! Please use +, -, *, or /.")        
        

