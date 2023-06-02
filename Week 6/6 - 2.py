n = int(input("Enter number:  "))
"""#dictionary method, IGNORE MODULE 4 STUFF
dict = {}

while n > 0:
    if n % 10 not in dict:
        dict[n % 10] = 1
    else:        
        dict[n % 10] += 1

    n //= 10

print(dict)"""

for i in range(10):
    count = 0
    temp = n
    while temp != 0:
        if temp % 10 == i:
            count += 1
        temp //= 10
    if count != 0:
        print(i, count)

    