import numpy as np
r=int(input("Enter the no of rows:"))
c=int(input("Enter the no of cols:"))
matrix=[]
for i in range(r):
	row=[]
	for j in range(c):
		val=int(input("Enter element:"))
		row.append(val)
	matrix.append(row)
new_matrix=np.array(matrix)
print("matrix is:")
print(new_matrix)
print("Trace of matrix:")
print(np.trace(new_matrix))
