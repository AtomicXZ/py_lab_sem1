def factorial(num):
    if num == 0:
        return 1
    else:
        return (num * factorial(num - 1))


def armstrong(num):
    n = m = num
    dig = 0
    sum = 0

    while n > 0:
        n //= 10
        dig += 1

    while m > 0:
        sum += (m % 10)**dig
        m //= 10

    return True if sum == num else False


def strong(num):
    n = num
    sum = 0

    while n > 0:
        sum += factorial(n % 10)
        n //= 10

    if sum == num:
        return True
    else:
        return False


def prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
            break
    else:
        return True


def perfect(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return True if sum == num else False


def magic(num):
    sum = 0
    while (num > 0 or sum > 9):
        if (num == 0):
            num = sum
            sum = 0
        sum = sum + num % 10
        num = num // 10

    return True if sum == 1 else False


n = int(input("Enter number:  "))

if n > 9:
    if armstrong(n):
        print("Armstrong number.")
    elif strong(n):
        print("Strong number.")
    elif magic(n):
        print("Magic number.")
elif prime(n):
    print("Prime number.")
elif perfect(n):
    print("Perfect number.")
else:
    print("Not a special number.")
