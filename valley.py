s = "DDUUUUDD"
se = "UDDDUDUU"

def countingValleys(n,s):
	height = 0
	valley_count = 0
	for i,elevation in enumerate(s):
		if (elevation == "U"):
			height += 1
		else:
			if height == 0:
				valley_count += 1
			height -= 1

	return (valley_count)

print(countingValleys(8,se))
