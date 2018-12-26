inpu = """4
aba
baba
aba
xzxb
3
aba
xzxb
ab
"""

inp = """100
lekgdisnsbfdzpqlkg
eagemhdygyv
jwvwwnrhuai
urcadmrwlqe
mpgqsvxrijpombyv
mpgqsvxrijpombyv
urcadmrwlqe
mpgqsvxrijpombyv
eagemhdygyv
eagemhdygyv
jwvwwnrhuai
urcadmrwlqe
jwvwwnrhuai
kvugevicpsdf
kvugevicpsdf
mpgqsvxrijpombyv
urcadmrwlqe
mpgqsvxrijpombyv
exdafbnobg
qhootohpnfvbl
suffrbmqgnln
exdafbnobg
exdafbnobg
eagemhdygyv
mpgqsvxrijpombyv
urcadmrwlqe
jwvwwnrhuai
lekgdisnsbfdzpqlkg
mpgqsvxrijpombyv
lekgdisnsbfdzpqlkg
jwvwwnrhuai
exdafbnobg
mpgqsvxrijpombyv
kvugevicpsdf
qhootohpnfvbl
urcadmrwlqe
kvugevicpsdf
mpgqsvxrijpombyv
lekgdisnsbfdzpqlkg
mpgqsvxrijpombyv
kvugevicpsdf
qhootohpnfvbl
lxyqetmgdbmh
urcadmrwlqe
urcadmrwlqe
kvugevicpsdf
lxyqetmgdbmh
urcadmrwlqe
lxyqetmgdbmh
jwvwwnrhuai
qhootohpnfvbl
qhootohpnfvbl
jwvwwnrhuai
lekgdisnsbfdzpqlkg
kvugevicpsdf
mpgqsvxrijpombyv
exdafbnobg
kvugevicpsdf
lekgdisnsbfdzpqlkg
qhootohpnfvbl
exdafbnobg
qhootohpnfvbl
exdafbnobg
mpgqsvxrijpombyv
suffrbmqgnln
mpgqsvxrijpombyv
qhootohpnfvbl
jwvwwnrhuai
mpgqsvxrijpombyv
qhootohpnfvbl
lekgdisnsbfdzpqlkg
eagemhdygyv
jwvwwnrhuai
kvugevicpsdf
eagemhdygyv
eagemhdygyv
lxyqetmgdbmh
qhootohpnfvbl
lxyqetmgdbmh
exdafbnobg
qhootohpnfvbl
qhootohpnfvbl
exdafbnobg
suffrbmqgnln
mpgqsvxrijpombyv
urcadmrwlqe
eagemhdygyv
lxyqetmgdbmh
urcadmrwlqe
suffrbmqgnln
qhootohpnfvbl
kvugevicpsdf
lekgdisnsbfdzpqlkg
lxyqetmgdbmh
mpgqsvxrijpombyv
jwvwwnrhuai
lxyqetmgdbmh
lxyqetmgdbmh
lekgdisnsbfdzpqlkg
qhootohpnfvbl
100
exdafbnobg
eagemhdygyv
mpgqsvxrijpombyv
kvugevicpsdf
lekgdisnsbfdzpqlkg
kvugevicpsdf
exdafbnobg
qhootohpnfvbl
eagemhdygyv
kvugevicpsdf
suffrbmqgnln
jwvwwnrhuai
lekgdisnsbfdzpqlkg
lekgdisnsbfdzpqlkg
mpgqsvxrijpombyv
jwvwwnrhuai
kvugevicpsdf
lekgdisnsbfdzpqlkg
exdafbnobg
suffrbmqgnln
qhootohpnfvbl
eagemhdygyv
exdafbnobg
suffrbmqgnln
jwvwwnrhuai
qhootohpnfvbl
eagemhdygyv
exdafbnobg
exdafbnobg
jwvwwnrhuai
qhootohpnfvbl
lxyqetmgdbmh
qhootohpnfvbl
suffrbmqgnln
lxyqetmgdbmh
qhootohpnfvbl
eagemhdygyv
jwvwwnrhuai
eagemhdygyv
qhootohpnfvbl
mpgqsvxrijpombyv
qhootohpnfvbl
jwvwwnrhuai
exdafbnobg
eagemhdygyv
eagemhdygyv
kvugevicpsdf
kvugevicpsdf
jwvwwnrhuai
urcadmrwlqe
lxyqetmgdbmh
qhootohpnfvbl
exdafbnobg
exdafbnobg
eagemhdygyv
qhootohpnfvbl
exdafbnobg
exdafbnobg
lekgdisnsbfdzpqlkg
jwvwwnrhuai
eagemhdygyv
urcadmrwlqe
kvugevicpsdf
lekgdisnsbfdzpqlkg
jwvwwnrhuai
eagemhdygyv
lekgdisnsbfdzpqlkg
exdafbnobg
kvugevicpsdf
jwvwwnrhuai
exdafbnobg
lxyqetmgdbmh
exdafbnobg
lxyqetmgdbmh
jwvwwnrhuai
mpgqsvxrijpombyv
eagemhdygyv
urcadmrwlqe
kvugevicpsdf
qhootohpnfvbl
jwvwwnrhuai
eagemhdygyv
urcadmrwlqe
urcadmrwlqe
exdafbnobg
qhootohpnfvbl
exdafbnobg
eagemhdygyv
exdafbnobg
jwvwwnrhuai
eagemhdygyv
jwvwwnrhuai
mpgqsvxrijpombyv
urcadmrwlqe
urcadmrwlqe
eagemhdygyv
eagemhdygyv
jwvwwnrhuai
suffrbmqgnln
eagemhdygyv"""

inp = list(inp.strip().split("\n"))
string_count = int(inp[0])
strings = []
for i in range(string_count):
	strings.append(inp[i+1])

query_count = int(inp[string_count + 1])
queries = []
for i in range(query_count):
	queries.append(inp[i + string_count + 2])

print(query_count, string_count)


def queryProcessed(ele, arr):
	for var in arr:
		if (ele == var):
			return True
	return False


def matchingStrings(strings, queries):
	query_count,string_count = len(queries),len(strings)
	result = [0 for x in range(query_count)]
	for i,query in enumerate(queries):
		for string in strings:
			if (query == string):
				if (not queryProcessed(query, queries[:i])):
					ind = i
					result[ind] += 1
				else:
					ind = queries.index(query)
					result[i] = result[ind]
	return (result)
print(matchingStrings(strings,queries))
