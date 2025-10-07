import numpy as np
n=int(input("Enter the no of row:"))
m=int(input("Enter the no of cols:"))
print("Enter the elements:")
matrix=[]
for i in range(n):
	a=[]
	for j in range(m):
		a.append(int(input()))
	matrix.append(a)
print("matrix elements are:")
for i in range(n):
	for j in range(m):
		print(matrix[i][j])
	print("");
print("invserse of array:")
print(np.linalg.inv(matrix))
