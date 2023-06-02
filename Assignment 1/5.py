list = []
check = False
loop1 = 9
loop2 = 2

while loop1 < 100:
    while (loop2 < (loop1//2)+1):
        if (loop1 % loop2 == 0):
            check = True
        loop2 += 1
    loop2 = 2

    if not check:
        print(loop1)
    check = False
    loop1 += 1

print(list)