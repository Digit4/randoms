sampleinp = ['programming', 'computer']
sampleinp1 = ['hello', 'World']
sampleinp2 = ['how', 'are']

def removeDuplicate(input1):
	input1 = [input1[x].lower() for x in range(len(input1))]
	input1list = list(input1[0])
	input2list = list(input1[1])
	
	if (input1[0] == input1[1]):
		return input1[0]

	for letter in input1list:
		for check in input2list:
			if check == letter:
				input2list.remove(check)
	
	return ("".join(input2list))
	
print(removeDuplicate(sampleinp))
