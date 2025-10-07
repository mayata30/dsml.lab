import matplotlib.pyplot as plt
import numpy as np
x1=np.array([1,2,6,18])
y1=np.array([3,10,12,20])
x2=np.array([3,5,7,14])
y2=np.array([2,9,17,19])
plt.plot(x1,y1,'o--r',mfc='g',ms='20',mec='g',label='line 1')
plt.plot(x2,y2,'o--b',mfc='y',ms='20',mec='y',label='line 2')
plt.title('Two line graph')
plt.legend()
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()
