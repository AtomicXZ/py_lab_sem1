# Write a Python Program to Put Even and Odd elements in a List into Two Different Lists
list = [12, 124, 14, 93, 9, -12, 921, -93]
o_list = []
e_list = []
for i in list:
    if i % 2 == 0:
        e_list.append(i)
    else:
        o_list.append(i)

print(f"Even list -> {e_list}\nOdd list -> {o_list}")