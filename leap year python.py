def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Input a number
n = int(input("Enter a number: "))

if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(n)
    print(f"The factorial of {n} is {result}")
  