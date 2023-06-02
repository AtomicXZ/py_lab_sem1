num = 32
n = m = num

numdig = 0
while n != 0:
    n //= 2
    numdig+=1

bin = 0
for i in range(numdig, 0, -1):
    bin = bin + (m%2)*(10**(numdig-i))
    m //= 2

print(bin)