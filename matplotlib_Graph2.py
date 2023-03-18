import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,20)
y1 = 2*x - 1
y2 = 5*x -5

plt.plot(x,y1,label='y=2x-1',color='red')
plt.plot(x,y2,label='y=5x-5',color='green')
plt.legend()
plt.show()