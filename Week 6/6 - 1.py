n = int(input("Enter number:  "))
num = n
rev = 0

while n != 0:
    rev = rev*10 + (n % 10)
    n //= 10
    
if rev == num:
    print(f"The number is a palindrome.")
else:
    print(f"The number is not a palindrome.")
