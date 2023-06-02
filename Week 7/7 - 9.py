# Write a Python Program to Find the Intersection of Two Lists
list1 = [1, 2, 4, 5, 6,]
list2 = [1, 5, 15, 7, 214, 12]
flist = []

for i in list1:
    if i in list1 and i in list2:
        flist.append(i)

print(flist)