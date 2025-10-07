import numpy as np

size=int(input("Enter the size: "))
#cols=int(input("Enter the number of columns: "))

matrix=[]

for i in range (size):
	row=[]
	for j in range (size):
		n=int(input('Enter the element: '))
		row.append(n)

	matrix.append(row)

print("The matrix is: ")
for row in matrix:
	print(row)

print("The determinant of the matrix is: ")
determinant=np.linalg.det(matrix)
print(int(determinant))
