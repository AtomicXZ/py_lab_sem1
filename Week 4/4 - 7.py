notes = [2000, 500, 200, 100, 50, 20, 10, 5]
amount = int(input("Enter amount:  "))
num = 0

for i in notes:
    num += amount//i
    amount %= i

print(f"There are {num} number of notes and {amount} amount in change.")