"""def factorial(num):
    if num == 0:
        return 1
    else:
        return (num * factorial(num-1))"""

"""x = int(input("Enter number:  "))
n = int(input("Number of iterations:  "))
loop = 1
sum = 0
fact = 1
while loop <= n:
    fact *= loop
    sum += (x**loop)/fact
    loop += 1

print(f"The sum of series is {format(sum, '.2f')}.")"""

x = int(input("Enter value of X:  "))
n = int(input("Enter value of n:  "))
loop = 1
sum = 0
fact = 1
while loop <= n:
    d = loop
    while d > 1:
        fact = fact * d
        d = d - 1
    sum = sum +(x**loop)/fact
    loop = loop + 1
    fact = 1

print("The sum of series is", sum)