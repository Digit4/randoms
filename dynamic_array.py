inp = """2 5
1 0 5
1 1 7
1 0 3
2 1 0
2 1 1
"""

n = inp.split("\n")
n.pop()
Q = []
for i in n:
    Q.append(list(map(int, i.split(" "))))



def dynamicArray(n, queries):
	lastAnswer = 0
	S0,S1 = [],[]
	for query in queries:
		if (query[0] == 1):
			if (query[1] == 0):
				S0.append(queries[(query[1] ^ lastAnswer) % n][-1])
			else:
				S1.append(queries[(query[1] ^ lastAnswer) % n][-1])
		elif (query[0] == 2):
			y = queries[(query[1] ^ lastAnswer) % n][-1]
			lastAnswer = y % len(queries)
			print(lastAnswer)
	return [S0,S1]
			
print(dynamicArray(Q[0][0],Q[1:]))
