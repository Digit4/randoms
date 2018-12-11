import math
lines = """2
1
2"""

all = list(map(int,lines.split("\n")))
T = all[0]
Narr = all[1:]
def handshakes(Narray):
	outarr = list()
	for N in Narray:
		outarr.append((N*(N-1))/2)
	return outarr

print(handshakes(Narr))