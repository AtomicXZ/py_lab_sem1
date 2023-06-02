from time import sleep

def sqrt(num):
    return num**(1/2)

t = int(input("Time in ms:  "))
i = int(input("Enter num:  "))
sleep(t*10**(-3)); print(f"Sqrt -> {sqrt(i)}\nWaited {t}ms before execution.")