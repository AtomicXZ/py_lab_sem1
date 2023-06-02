char = input("Enter char to get string after:  ")
string = "apple"

for i in range(-1, -len(string), -1):
    if string[i] == char:
        index = i
        break
else:
    print(f"Char '{char}' not in the string.")
    index = None

if index is not None:
    print(string[index+1:])