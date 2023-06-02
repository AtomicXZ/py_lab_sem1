def sum(num):
    if num == 0:
        return 0
    else:
        return (num%10 + sum(num//10))

n = int(input("Enter no:  "))
print(sum(n))