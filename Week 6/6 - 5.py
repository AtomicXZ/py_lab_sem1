# same as 3 - 5

def factorial(num):
    if num == 0:
        return 1
    else:
        return (num * factorial(num-1))

num = int(input("Enter number:  "))
print(f"Factorial is {factorial(num)}.")