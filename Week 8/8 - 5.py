"""Write a Python program to replace last value of tuples in a list.
Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]"""

tupe = [(41, 34, 73), (74, 14, 1), (57, 7, 63, 67)]
print([i[:-1] + (100,) for i in tupe])