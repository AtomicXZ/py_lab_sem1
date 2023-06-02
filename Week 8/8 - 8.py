# Write a Python program to find the highest 3 values of corresponding keys in a dictionary
dict = {"a":3245,1:65, "b":76, 8:95, "c":578,}
x = list(dict.values())
x.sort(reverse=True)

for j in x[:3]:
    for i in dict:
        if dict[i] == j:
            print(f"{i}: {j}")
