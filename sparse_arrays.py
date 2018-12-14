inp = """4
aba
baba
aba
xzxb
3
aba
xzxb
ab
"""

inp = list(inp.strip().split("\n"))
string_count = int(inp[0])
strings = []
for i in range(string_count):
	strings.append(inp[i+1])

query_count = int(inp[string_count + 1])
queries = []
for i in range(query_count):
	queries.append(inp[i + string_count + 2])


def matchingStrings(strings, queries):
	result = [0 for x in range(query_count)]
	print (result)
	for query in queries:
		for string in strings:
			if (query == string):
				ind = queries.index(query)
				result[ind] += 1
	return (result)
print(matchingStrings(strings,queries))