"""Write a Python program to remove an empty tuple(s) from a list of tuples. 
Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
"""
tupe = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
cum = [val for val in tupe if val]
print(cum)