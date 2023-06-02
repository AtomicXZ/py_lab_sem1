n = int(input("Enter number:  "))

for i in range(1, n//2+1):
    if n % i == 0:
        print(i, end=", ")
else:
    (print(n))