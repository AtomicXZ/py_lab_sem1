num1 = float(input("Enter number 1:  "))
num2 = float(input("Enter number 2:  "))
num3 = float(input("Enter number 3:  "))

if num1 == num2 == num3:
    print(f"Numbers are equal, 3 times their sum is {9*num1}")
else:
    print(f"The sum of numbers is {num1+num2+num3}")
