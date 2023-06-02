# Triangle 
s1 = float(input("Enter the length of first side of triangle:  "))
s2 = float(input("Enter the length of second side of triangle:  "))
s3 = float(input("Enter the length of third side of triangle:  "))
sp = (s1+s2+s3)/2

print(f"The perimeter of triangle is {s1+s2+s3} units and the area of triangle is {(sp*(sp-s1)*(sp-s2)*(sp-s3))**(1/2)}.")

# Circle
pi = 3.14
radius = float(input("Enter radius of circle:  "))

print(f"The circumference of the circle is {2*pi*radius} and the area of the circle is {pi*radius*radius}.")