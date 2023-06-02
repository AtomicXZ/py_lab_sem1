n = int(input("no of rows:  "))

m = 2
for i in range(n):
    for j in range(i+1):
        count = 0
        while not count:
            check = False
            for i in range(2, m//2+1):
                if m % i == 0:
                    check = True
            if not check:
                print(m, end=" ")
                count += 1
            m += 1
    print()
