"""
amount = P( 1 + R/100) ** T
CI = AMOUNT - P
"""

principal=float(input("enter principal amount: "))
rate=float(input("enter rate of interest: "))
time=float(input("enter time duration: "))

amount1 = principal * ( 1 + rate/100 ) ** time
amount2 = principal * pow(( 1 + rate/100 ), time)
print(round(amount1,2))

ci = amount1 - principal
print("compound interest is ",round(ci))