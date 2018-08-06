series = [1,5,7,9,9]#[0,653,1854,4063]
one = 0
def check_series(s1):
	check = 0
	for element in s1:
		if element == 0:
			check+=1
	if check < len(s1):
		return True
	else:
		return False
length = len(series)
steps = 1
while(check_series(series)):
	new_series = list()
	for index in range(length):
		upper = (index+1)%length
		lower = index
		one = series[upper] - series[lower]
		one = abs(one)
		new_series.append(one)
	#print (new_series)
	for i,v in enumerate(new_series):
		series[i] = v
	steps +=1
	print (series)

print(steps," steps")
