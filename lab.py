import math
from datetime import datetime
#1.
first = input("Enter your first name: ")
#2.
last = input("Enter your last name: ")
#3.
print("Hello", first.upper(),last.lower())
#4.
print("\n\n")
#5. 
name = (first + " " + last)
#6. 
print("Hello "+ name.removesuffix(last))
#7
print(name.replace(last, last+", Walsh College Student"))
#8
print('"Start by doing what\'s necessary; then do what\'s possible; and suddenly you are doing the impossible - Francis of Assisi"')
#9
x = 1.02
y = 2.01
#10
add = x + y
sub = x - y
mu = x * y
div = x / y
#11
print(x, "+", y, "=", add)
print("%.2f %s %.2f %s %.2f" %(x,"-",y,"=",sub))
print('{0} * {1} = {2}'.format(x, y, mu))
print(f"{x} / {y} = {div}")
#12
sq_root = math.sqrt(mu)
print("The square root of", round(mu,2), "=", round(sq_root,2))
#13
month = datetime.now().strftime("%B")
day = datetime.now().day
#14
print(f"\n\t\tToday is day {day} of the month of {month}")

