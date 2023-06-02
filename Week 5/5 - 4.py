n = int(input("Enter number:  "))

last = n % 10

while n > 9:
    n //= 10

print(f"First digit is {n} and last digit is {last}.")