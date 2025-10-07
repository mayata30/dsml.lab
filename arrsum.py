import numpy as np
ls=[[1,2,3],[8,4,2]]
arr=np.array(ls)
print(arr)
sum1=np.sum(arr)
sum2=np.sum(arr,axis=1)
sum3=np.sum(arr,axis=0)
print("sum=",sum1)
print("sumrow=",sum2)
print("sumcolumn=",sum3)
