print("A quadratic equation is of the form ax^2 + bx + c")
a = int(input("Enter the value of a:  "))
b = int(input("Enter the value of b:  "))
c = int(input("Enter the value of c:  "))

d = (b**2 - 4*a*c)**(1/2)

print(f"The roots of the equation are {(-b+d)/(2*a)} and {(-b-d)/(2*a)}")