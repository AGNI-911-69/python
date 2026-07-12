"""
when all the length of the sides of the triangle is known - a,b,c
semi perimeter (S)= (a+b+c)/2
area = square root of (s*(s-a)*(s-b)*(s-c))
"""

a=float(input("enter first side of triangle: "))
b=float(input("enter second side of triangle: "))
c=float(input("enter third side of triangle: "))

s=(a+b+c)/2
area= (s * (s-a) * (s-b) * (s-c))** 0.5
print("area of triangle is ",round(area,2))


