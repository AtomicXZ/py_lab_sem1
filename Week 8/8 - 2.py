# Write a Python program to find the repeated items of a tuple
def nuke_all(arr, cm):
    return [val for val in arr if val != cm]


tupe = (8, 3, 6, 9, 8, 9, 3, 8, 8, 1, 9, 8, 5, 3, 6)
print("Element\tCount")
for i in tupe:
    ct = tupe.count(i)
    if ct > 1:
        print(f"{i}\t{ct}")
        tupe = nuke_all(tupe, i)

"""    count = 0
    for j in tupe:
        if j == i:
            count += 1
    if count > 1:
        print(i)"""