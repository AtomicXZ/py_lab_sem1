n = int(input("no of rows:  "))

for i in range(n):
    for j in range(n+i):
        if (j == n - i - 1) or (j == n + i - 1):
            print("*", end="")
        else:
            print(end=" ")
    print()
for i in range(n-2, -1, -1):
    for j in range(n+i):
        if (j == n - i - 1) or (j == n + i - 1):
            print("*", end="")
        else:
            print(end=" ")
    print()    

