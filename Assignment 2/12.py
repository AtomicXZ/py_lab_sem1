n = int(input("no of rows:  "))

for i in range(1, n+1):
    for j in range(n):
        if i == 1 or i == n:
            print("*", end=" ")
        elif j == (n-i):
            print("*", end=" ")
        else:
            print(end="  ")
    print()
