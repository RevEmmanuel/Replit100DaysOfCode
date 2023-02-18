def factorial(value):
  if value == 1 or value == 0:
    return 1
  else:
    return value * factorial(value-1)


number = int(input("Enter number to find factorial: > "))
print(f"The factorial of {number} is {factorial(number)}")
