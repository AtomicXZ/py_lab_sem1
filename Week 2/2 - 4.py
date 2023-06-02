a = input("Enter first variable:  ")
b = input("Enter second variable:  ")

print(f"First variable is {a} and second variable is {b}.")

temp = a
a = b
b = temp

print(f"After swapping, first variable is {a} and second variable is {b}")