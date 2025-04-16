#Input the matrix dimentions
rows=int(input("Enter the number of rows in the matrix:"))
cols=int(input("Enter the number of columns in the matrix:"))

#Input the matrix
matrix=[]
print("Enter the matrix row by row:")
for i in range(rows):
    row=list(map(int,input().split()))
    matrix.append(row)
#Input the value of K
k=int(input("Enter the value of K:"))

#Process the matrix
for i in range(rows):
    if(i+1)%k==0: #Check if it's the Kth row(1based index)
        matrix[i]=matrix[i][::-1] #Reverse the row

    #Output the updated matrix
    print("Updated Matrix:")
for row in matrix:
    print(*row)