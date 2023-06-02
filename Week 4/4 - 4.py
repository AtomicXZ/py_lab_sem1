char = input("Enter the character:  ")

if (char >= "A" and char <= "Z") or (char >= "a" and char <= "z"):
    print("Alphabet.")
elif (char >= "0" and char <= "9"):
    print("Number.")
else:
    print("Special character.")