import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
sizes = np.random.rand(50)*100

plt.scatter(x,y,c=colors,s=sizes,alpha=0.2, cmap='plasma')
plt.colorbar()
plt.show()

