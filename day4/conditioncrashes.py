try:
  a = int(input("enter a number:"))
  b = int(input("enter a divisor:"))
  result = a / b
  print(f"Result: {result}")
except ZeroDivisionError:
  print("cannot divide by zero")
except ValueError:
  print("Please enter a valid number")
except Exception as e:
  print(f"Unexpected error: {e}")