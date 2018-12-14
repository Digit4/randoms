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
	seq = []
	for x in range(n):
		seq.append([])
	for query in queries:
		a,x,y = query[0:3]
		if (a == 1):
			toBeAdded = queries[(x ^ lastAnswer) % n][-1]
			seq[((x ^ lastAnswer) % n)].append(y)
		elif (query[0] == 2):
			pass
	return seq
			
print(dynamicArray(Q[0][0],Q[1:]))
