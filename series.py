#Input the value of x and n
x=float(input("Enter the value of x:"))
n=int(input("Enter the number of terms (n):"))

#Initialize the sum and factorial
sum_series=0
factorial=1

#Compute the series
for i in range(n):
    if i>0:
        factorial*=i #Compute factorial iteratively
    term=((-1)**i)*(x**i)/factorial #Compute the sum
    sum_series+= term #Add the term to the sum

#Output the result
print("The sum of the series up to n term is:",sum_series)