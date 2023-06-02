n = int(input("Enter value of n:  "))
a = 0
b = 1

if n > 2:
    print(f"{a}, {b}", end=", ")
    for i in range(1, n-2):
        temp = a + b
        a = b
        b = temp
        print(b, end=", ")
    else:
        print(a+b)
else:
    print("Please input n value > 2.")