#answer to below array is 3
ar = [10,20,20,10,10,30,10,20]
arr = [1,1,3,1,2,1,3,3,3,3]
def isin(ele,el):
	for j in el:
		if ele == j:
			return True
	return False

def checkPairs(arr):
	pairs = list()
	i,pair_count = 0,0
	for sock in arr:
		if (isin(sock,pairs)):
			pairs.remove(sock)
			pair_count += 1
		else:
			pairs.append(sock)
	return pair_count




print(checkPairs(arr))
