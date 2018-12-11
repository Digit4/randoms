import sys
print (sys.version)
class Car():
	def __init__(self,clr,category):
		self.color = clr
		self.type = category
		print("Object Created Successfully!")

honda = Car("red","sedan")
print (honda.__dict__)
