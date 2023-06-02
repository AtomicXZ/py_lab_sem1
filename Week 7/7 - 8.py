# Write a Python Program to Find the Union of two Lists

list1 = [1, 2, 4, 5, 6,]
list2 = [1, 5, 15, 7, 214, 12]
mlist = list1 + list2
flist = []

for i in mlist:
    if i not in flist:
        flist.append(i)

print(flist)
