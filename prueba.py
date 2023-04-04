import math
import matplotlib.pyplot as plt
import numpy as np

x=np.array([-5,5,0.1])
y=[]
for i in x:
    y.append(math.sin(i))

plt.plot(y)
plt.show()