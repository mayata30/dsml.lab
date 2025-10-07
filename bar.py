import matplotlib.pyplot as plt
import numpy as np
prg=np.array(["java","python","javascript","c#","c++"])
pop=np.array([22.2,17.6,8.8,7.7,6.7])
color=["red","green","yellow","blue","black"]
plt.barh(prg,pop,color=color)
plt.xlabel("program language")
plt.ylabel("popularity")
plt.title("barchart")
plt.show();
