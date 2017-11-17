from re import sub
from decimal import Decimal

money = '-6,150,593.22'

value1 = Decimal(sub(r'[^\d.]', '', money))
value2 = Decimal(sub(r'[^\d\-.]', '', money))

print(value1)
print(value2)
