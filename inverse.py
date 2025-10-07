import numpy as np
r=int(input("Enter the number of rows:"))
c=int(input("Enter the number of cols:"))
matrix=[]
for i in range(r):
    row = []
    for j in range(c):
        val=int(input("Enter element:"))
        row.append(val)
    matrix.append(row)
new_matrix=np.array(matrix)
print("matrix elements are:")
print(new_matrix)
print("inverse of matrix:")
print(np.linalg.inv(new_matrix))
