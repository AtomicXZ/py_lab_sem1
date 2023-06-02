n = int(input("Which index to remove?  "))
string = "CSE"

if n > len(string) - 1 or n < -len(string):
    print("Index out of bounds")
else:
    print(string[:n] + string[n+1:])