import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

x = input("Enter x coordinate values (seperated by comma (,)): ")
x_og = x
x = x.replace(" ", "").split(",")

y = list()

quadratic = input("Enter quadratic equation: ")
quadratic = quadratic.replace("^", "**")

def f(value):
    factors = []
    for i in range(1, int(value**0.5)+1):
        if value % i == 0:
            factors.append((i, value / i))
    return factors

counts = Counter(quadratic)
count = 0
for symbol in counts:
   if symbol in ["-"]:
       count += counts[symbol]

for xaxis in x:
	quadratic = quadratic.replace("x", "")

if counts['-'] == 0:
	quadratic = quadratic.split("+")
	print("a")
if counts['-'] == 1:
	minus_pos = [pos for pos, char in enumerate(quadratic) if char == "-"]
	quadratic = quadratic.replace("-", "+m").split("+")
	print("b")
if counts['-'] == 2:
	quadratic = quadratic.replace("-", "+m").split("+")
	print(quadratic)

del quadratic[0]

if 'm' in quadratic[0]:
	quadratic[0] = quadratic[0].replace("m", "-")
if 'm' in quadratic[1]:
	quadratic[1] = quadratic[1].replace("m", "-")
print(quadratic)

if counts['-'] == 1:
	factors = f(int((quadratic[1]).replace("-", "")))
	print(factors)
	factors = '-'+factors # left of here 17.11.21
elif counts['-'] == 2 or 0:
	factors = f(int((quadratic[1]).replace("-", "")))

for factorpair in factors:
	if str((eval(str(factorpair).replace(" ", "").replace(",","+")))) == str(quadratic[0]+".0"):
		found_fpair = str(factorpair).replace("(", "").replace(")", "").replace(" ", "").replace(".0", "").split(",")
		print(found_fpair)

print(found_fpair)

if counts['-'] == 0:
	print(f"(x+{found_fpair[0]})(x+{found_fpair[1]})")
elif counts['-'] == 1:
	if '-' in quadratic[0]:
		print(f"(x-{found_fpair[0]})(x-{found_fpair[1]})")
	elif '-' in quadratic[1]:
		print(f"(x)(x)")
elif counts['-'] == 2:
	print(f"(x+{found_fpair[0]})(x-{found_fpair[1]})")
print(str(quadratic) + " - quadratic")
#plt.plot(x_og, y)
#plt.show()