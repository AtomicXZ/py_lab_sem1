n = int(input("no of rows:  "))

for i in range(n, 0, -1):
    for j in range(n-i):
        print(end=" ")
    for j in range(2*i-1):
        print(i, end="")
    print()