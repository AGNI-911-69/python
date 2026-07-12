"""
simple interest = (P * R * T)/100
P =principal amount
R =rate of interest
T =time duration
"""

principal=float(input("enter principal amount: "))
rate=float(input("enter rate of interest: "))
time=float(input("enter time duration: "))

si = (principal * rate * time)/100
print("simple interest is ",si)
