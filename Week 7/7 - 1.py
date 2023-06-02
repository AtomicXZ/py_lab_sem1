# Write a Python Program to Find the Largest Number in a List 

list = input("Enter numbers (comma separated):  ")
list = list.split(",")
for i in range(len(list)):
    list[i] = float(list[i])

max = list[0]
for i in list:
    if i > max:
        max = i
print(f"Max is {max}")