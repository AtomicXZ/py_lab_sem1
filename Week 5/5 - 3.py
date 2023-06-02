n = abs(int(input("Enter number:  ")))
d = 0

while n != 0:
    n //= 10
    d += 1

print(f"The number has {d} digits.")
