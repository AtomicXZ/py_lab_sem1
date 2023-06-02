num = float(input("Enter number:  "))

if abs(1000 - num) < 100:
    print("Number within 100 of 1000.")
elif abs(2000 - num) < 100:
    print("Number within 100 of 2000.")