import random

print ("##########DICE ROLLER##########")

def roll_it(number_of_dice,amount):
	for i in range(number_of_dice):
			print (random.randint(0,amount))

def parse_line(sentence):
	fragments = sentence.split("d")
	return fragments

inp = "1"

while (inp != "0"):
	inp = str(input())
	list_inp = parse_line(inp)
	if len(list_inp) == 1 or list_inp[0] == "":
		dice_count = 1
	else:
		dice_count = int(list_inp[0])
	dice_faces = int(list_inp[1])
	roll_it(dice_count,dice_faces)