inp1 = """5 3
1 2 100
2 5 100
3 4 100
"""

inp2 = open("test.txt", 'r')
inp2 = inp2.readlines()
x = []
for i in inp2:
	i = i.strip()
	i = list(map(int,i.split()))
	x.append(i)

inp2 = x
inp1 = list(map(str, inp1.strip().split('\n')))

y =[]
def parse(inp1):
	for i in inp1:
		i = list(map(int, i.split()))
		y.append(i)

	inp1 = y
	return inp1

inp1 = parse(inp1)
print(len(inp2[1:]))

def addValue(arr, val):
	temp = []
	for i in arr:
		i += val
		temp.append(i)
	return temp

def findMax(arr):
	temp = -1
	for ele in arr:
		if temp < ele:
			temp = ele
	return temp

def arrayManipulation(n, queries):
	array = [0 for i in range(n+1)]
	for query in queries:
		if(len(query) == 3):
			start_from = query[0]
			go_to = query[1]+1
			insertion = query[2]
			array[start_from:go_to] = [x+insertion for x in array[start_from:go_to]]
			# array[start_from:go_to] = addValue(array[start_from:go_to], insertion)
			#print(array[1:])
		elif(len(query) == 2):
			index = query[0]
			insertion = query[1]
			array[index] += insertion
			print(len(query),index,insertion)
	return findMax(array[1:n+1])

print(arrayManipulation(inp2[0][0],inp2[1:]))
