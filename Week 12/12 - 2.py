char = "a" #input("Enter char to check:  ")
string = "An apple is called an apple because it is an apple."

num = 0
for i in string:
    if i == char:
        num += 1

print(f"Char \"{char}\" occured {num} times.")