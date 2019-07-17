from math import fabs

fi = open('ainp.txt', 'r')

lines = fi.readlines()

num_houses = int(lines[0].strip("\n"))
house_array = list(map(int, lines[1].rstrip("\n").split(" ")))
r_val = int(lines[2].rstrip())

# print("Number of houses: {}\nHouse Array: {}\nRange: {}".format(num_houses,house_array,r_val))


def st2(houses, r):
	for i in range(len(houses)):
		flag = 0
		for j in range(len(houses)):
			if (fabs(houses[j] - houses[i]) > r):
				flag = 1
		if flag != 1:
			return houses[i]



def calculateAntennas(n, arr, r):
	dist = 0
	grp1,antenna_loc = [],[]
	fsi = 0
	for i in range(n-1):
		j = i + 1
		print("House:{}".format(arr[i]))
		dist += arr[j] - arr[i]
		if (dist <= 2*r + 1):
			grp1.append(arr[i])
		else:
			antenna_loc.append(st2(grp1, r))
			# grp1 = []
			dist = 0


	print(grp1)
	print(antenna_loc)

calculateAntennas(num_houses,house_array,r_val)