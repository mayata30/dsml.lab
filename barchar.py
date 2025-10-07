import matplotlib.pyplot as plt
import numpy as np
plt.title("program language and popularity graph")
prg=np.array(["java","python","java script","c#","c++"])
pop=np.array([22.2,17.6,8.8,7.7,6.7])
plt.bar(prg,pop,color="green",width=0.3)
plt.xlabel("program_language")
plt.ylabel("popularity")
plt.show()
