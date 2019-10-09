# Calculator that calculates total based on QUANTITY of coins/bills etc.

pennies = input("Number of Pennies: ")
num1 = int(pennies) * float(.01)
print(num1)
nickels = input("Number of Nickels: ")
num2 = int(nickels) * float(.05)
print(num2)
dimes = input("Number of Dimes: ")
num3 = int(dimes) * float(.1)
print(num3)
quarters = input("Number of Quarters: ")
num4 = int(quarters) * float(.25)
print(num4)

singles = input("Number of Singles: ")
num5 = int(singles)
print(num5)
fives = input("Number of Fives: ")
num6 = int(fives) * 5
print(num6)
tens = input("Number of Tens: ")
num7 = int(tens) * 10
print(num7)
twenties = input("Number of Twenties: ")
num8 = int(twenties) * 20
print(num8)

print(float(num1) + float(num2) + float(num3) + float(num4) + float(num5) + float(num6) + float(num7) + float(num8))
