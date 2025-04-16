def fibo_rec(n):			#function declaration
	if n==1:
		return n
	else:
		return (fibo_rec(n-1)+fibo_rec(n-2))

nterms=int(input("Enter the term no:"))
if(nterms<=0):
	print("Enter a valid term")
else:
	print("Fibonacci series:")
	for i in range(nterms):
		print(fibo_rec(i))
