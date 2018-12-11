import math
inp = """4 1
3 10 2 9
7"""

inp = list(map(str,inp.split('\n')))
fl = list(map(int,inp[0].split(" ")))
sl = list(map(int,inp[1].split(" ")))
la = int(inp[2])

def bonAppetit(bill,k,b):
	pay = 0
	for i,item in enumerate(bill):
		if (i != k):
			pay += item

	pay = pay / 2
	diff = b - pay

	if (diff == 0):
		return "Bon Appetit"
	else:
		return int(diff)

print(bonAppetit(sl,fl[1],la))
