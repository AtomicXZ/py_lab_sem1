n = int(input("Enter number:  "))
rev = 0

while n != 0:
    rev = rev*10 + (n % 10)
    n //= 10
    

print(f"The reverse of the number is {rev}.")
