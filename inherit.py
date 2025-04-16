class fruit:
	#constructor
	def __init__(self,s,c):
		self.shape=s
		self.color=c
	def display(self):
		print("within fruit class")
		print(self.shape)
		print(self.color)


a1=fruit("circle","red")
a1.display()

class apple(fruit):
	def display(self):
		print("within fruit class")
		print(self.shape)
		print(self.color)

a2=apple("oval","green")
a2.display()
