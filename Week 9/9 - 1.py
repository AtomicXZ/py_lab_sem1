def fact(num):
    if num == 0:
        return 1
    else:
        return (num * fact(num - 1))


def combination(n, r):
    return (fact(n) // (fact(r) * fact(n - r)))


n = int(input("rows:  "))

for i in range(n):
    for j in range(n - i + 1):
        print(end=" ")
    for j in range(i + 1):
        print(combination(i, j), end=" ")
    print()