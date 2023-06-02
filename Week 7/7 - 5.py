# Write a Python Program to Sort the List According to the Second Element in Sublist
list = [["a", 100], ["b", 0], ["c", -100], ["d", 90], ["e", 78]]

for i in list:
    for j in range(len(list)-1):
        if list[j][1] > list[j+1][1]:
            temp = list[j]
            list[j] = list[j+1]
            list[j+1] = temp

print(list)