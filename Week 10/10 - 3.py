def hcf(a, b): #GCD
    if not b:
        return a
    else:
        return hcf(b, a%b)

print(hcf(30.5, 61))