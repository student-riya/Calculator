a=[2,4,5,9]
print(a[3])

try:
	print(a[3])
	d=a[2]/0
except IndexError as Ie:
	print("Index is larger than the length of the list")
except ZeroDivisionError as Ze:
	print("divide by zero problem")
except:
	print("There has been some problem")


