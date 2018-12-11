inp = """11
1 2 3 4 5 4 3 2 1 3 4"""
"""6
1 4 4 4 5 3"""

conv = list(map(str,inp.split("\n")))
n = int(conv[0])
arr = list(map(int,conv[1].split(" ")))

def isin(item,array):
	for i in array:
		if i == item:
			return False
	return True

def select_max(li):
	ret = [0,0,0,0,0]
	for ele in li:
		ret[ele-1] += 1
	return (ret)

def find_max(arr):
	maxi,prev,pos = 0,0,[-1]
	for i,v in enumerate(arr):
		if (v > maxi):
			maxi = v
			if (v == maxi and not isin(maxi,pos)):
				pos.append(i)
			if pos[0] != i:
				pos[0] = i
	pos.sort()
	return pos


def migratoryBirds(ar):
	storage = select_max(ar)
	maximum = find_max(storage)
	return (maximum[0] + 1)

print(migratoryBirds(arr))
