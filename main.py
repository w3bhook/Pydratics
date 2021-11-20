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
    value = int(value)
    factors = []
    if value > 0:
        for i in range(1,value+1):
            if value % i == 0:
                factors.append((i, value / i))
        return factors
    elif value < 0: 
        for i in range(value,0):
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
if counts['-'] == 1:
	minus_pos = [pos for pos, char in enumerate(quadratic) if char == "-"]
	quadratic = quadratic.replace("-", "+m").split("+")
if counts['-'] == 2:
	quadratic = quadratic.replace("-", "+m").split("+")

del quadratic[0]

if 'm' in quadratic[0]:
	quadratic[0] = quadratic[0].replace("m", "-")
if 'm' in quadratic[1]:
	quadratic[1] = quadratic[1].replace("m", "-")

if counts['-'] == 0:
	factors = f(int(quadratic[1]))
elif counts['-'] == 1:
	factors = f(int((quadratic[1]).replace("-", "")))
	i = 0
	for fac in factors:
		while i <= 1:
			print(fac)
			print(i)
			factors[i] = tuple(str(str(fac).replace(fac, '-'+fac)))
			i +=1
elif counts['-'] == 2:
	factors = f(int(quadratic[1]))

for factorpair in factors:
	if str((eval(str(factorpair).replace(" ", "").replace(",","+")))) == str(quadratic[0]+".0"):
		found_fpair = str(factorpair).replace("(", "").replace(")", "").replace(" ", "").replace(".0", "").split(",")

	elif str((eval(str(factorpair).replace(" ", "").replace(",","-")))) == str(quadratic[0]+".0"):
		found_fpair = str(factorpair).replace("(", "").replace(")", "").replace(" ", "").replace(".0", "").split(",")

	if str((eval((str(factorpair).replace(" ", "").replace(",","+").split('+'))[0]+"-"+(str(factorpair).replace(" ", "").replace(",","+").split('+'))[1]))) == str(quadratic[0]+".0"):
		found_fpair = str(factorpair).replace("(", "").replace(")", "").replace(" ", "").replace(".0", "").split(",")

if counts['-'] == 0:
	if found_fpair[0] != found_fpair[1]:
		print(f"(x+{found_fpair[0]})(x+{found_fpair[1]})")
	elif found_fpair[0] == found_fpair[1]:
		print(f"(x+{found_fpair[0]})(x-{found_fpair[1]})")
elif counts['-'] == 1:
	if '-' in quadratic[0]:
		if '-' not in quadratic[1]:
			print(f"(x-{found_fpair[0]})(x-{found_fpair[1]})")
	elif '-' in quadratic[1]:
		if '-' in quadratic[0]:
			print(f"(x-{found_fpair[0]})(x+{found_fpair[1]})")
elif counts['-'] == 2:
	if '-' in found_fpair[0]:
		print(f"(x{found_fpair[0]})(x+{found_fpair[1]})")
	elif '-' in found_fpair[1]:
		print(f"(x+{found_fpair[0]})(x-{found_fpair[1]})")
#plt.plot(x_og, y)
#plt.show()