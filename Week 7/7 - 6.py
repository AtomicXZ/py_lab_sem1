# Write a Python Program to Find the Second Largest Number in a List Using Bubble Sort

list = [1, 2, 49, -10, 11]

for i in list:
    for j in range(len(list)-1):
        if list[j] > list[j+1]:
            temp = list[j]
            list[j] = list[j+1]
            list[j+1] = temp

print(list[-2])