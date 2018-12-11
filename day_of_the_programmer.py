def checkLeap(year):
	if (year > 1918):
		if (year%400 == 0):
			return True
		if (year % 4 == 0 and not year % 100 == 0):
			return True
	elif (year < 1918):
		if (year%4 == 0):
			return True
	return False

def return_days_of_month(month):
	days = [31,30,31,30,31,30,31,31,30,31,30,31]
	return days[month]

def dayOfProgrammer(year):
	days,date,prev,selected = 0,0,0,0
	month = 0
	while (days < 256):
		if month == 1:
			if checkLeap(year):
				days -= 1
			else:
				days -= 2
			if (year == 1918):
				days -= 13
		selected = return_days_of_month(month)
		prev = days
		days += selected
		month += 1
		print ("month:",month,"selected:",selected,"days:",days)
	while (prev <= 256):
		prev+= 1
		date += 1
	if month//10 == 0:
		new_month = "0"+str(month)
	else:
		new_month = str(month)
	print(new_month)
	whole_date = ".".join([str(date-1),new_month,str(year)])
	return whole_date

n = int(input("Enter year:"))
print (checkLeap(n))
print(dayOfProgrammer(n))
