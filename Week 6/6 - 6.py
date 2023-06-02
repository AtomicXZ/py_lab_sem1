n = int(input("Enter upper bound:  "))

for i in range(2, n+1):
    check = False
    for j in range(2, i//2+1):
        if (i % j == 0):
            check = True

    if not check:
        print(i, end=", ")
print("\b\b  ")
