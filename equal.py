import numpy as np
arr1=np.array([1,2,3,4])
arr2=np.array([1,2,4,4])
print(arr1)
print(arr2)
if np.array_equal(arr1,arr2):
	print("equal")
else:
	print("not equal")
