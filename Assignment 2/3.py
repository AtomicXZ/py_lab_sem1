n = int(input("no of rows:  "))

for i in range(1, n+1):
    for j in range(n):
        if j >= (n-i):
            print("*", end="")
        else:
            print(end=" ")
    print()